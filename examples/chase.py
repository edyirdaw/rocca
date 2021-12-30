# Define an agent for the Chase env with OpencogAgent

##############
# Initialize #
##############

# Python
import time

# OpenAI Gym
import gym

# OpenCog
from opencog.type_constructors import (
    ExecutionLink,
    SchemaNode,
    EvaluationLink,
    PredicateNode,
    NumberNode,
    ConceptNode,
)
from opencog.utilities import set_default_atomspace
from opencog.pln import *
from opencog.ure import ure_logger
from opencog.logger import log

# OpenCog Gym
from rocca.agents import OpencogAgent
from rocca.agents.utils import *
from rocca.envs.wrappers import GymWrapper

import os
from os.path import exists
import subprocess
import logging

env = gym.make("Chase-v0")
# Uncomment the following to get a description of env
# help(env.unwrapped)

#################
# Chase Wrapper #
#################
# TODO: move to a library module.
class ChaseWrapper(GymWrapper):
    def __init__(self, env, atomspace):
        action_list = ["Go Left", "Go Right", "Stay", "Eat"]
        super().__init__(env, atomspace, action_list)

    def labeled_observation(self, space, obs, sbs=""):
        """Translate gym observation to Atomese

        There are 2 gym observations:

        Agent Position is 0 (left) or 1 (right)
        Pellet Positon is 0 (left), 1 (right) or 2 (none)

        Translated in Atomese as follows:

        Evaluation
          Predicate "Agent Position"
          AP

        where AP can be

        1. Concept "Left Square"
        2. Concept "Right Square"

        Evaluation
          Predicate "Pellet Position"
          PP

        where PP can be

        1. Concept "Left Square"
        2. Concept "Right Square"
        3. Concept "None"

        """

        to_atomese_position = {
            0: ConceptNode("Left Square"),
            1: ConceptNode("Right Square"),
            2: ConceptNode("None"),
        }
        ap = to_atomese_position[obs[0]]
        pp = to_atomese_position[obs[1]]
        return [
            EvaluationLink(PredicateNode("Agent Position"), ap),
            EvaluationLink(PredicateNode("Pellet Position"), pp),
        ]


###############
# Chase Agent #
###############


class ChaseAgent(OpencogAgent):
    def __init__(self, env, atomspace):
        set_default_atomspace(atomspace)

        # Create Action Space. The set of allowed actions an agent can take.
        # TODO take care of action parameters.
        action_space = {ExecutionLink(SchemaNode(a)) for a in env.action_names}
        # print('action_space::::::::::::::::::::\n', action_space,'\nend_action_space::::::::::::::::::::')

        # Create Goal
        pgoal = EvaluationLink(PredicateNode("Reward"), NumberNode("1"))
        ngoal = EvaluationLink(PredicateNode("Reward"), NumberNode("0"))

        # print('pgoal::::::::::::::::::::\n', pgoal,'\nend_pgoal::::::::::::::::::::')


        # Call super ctor
        OpencogAgent.__init__(self, env, atomspace, action_space, pgoal, ngoal)

        # Overwrite some OpencogAgent parameters
        self.polyaction_mining = False
        self.monoaction_general_succeedent_mining = True
        self.temporal_deduction = True
        self.true_cogscm = True
        self.empty_vardecl_cogscm = True


if __name__ == "__main__":
    # Set main atomspace
    atomspace = AtomSpace()
    set_default_atomspace(atomspace)

    # Init loggers
    log.set_level("info")
    # log.set_sync(True)
    agent_log.set_level("debug")
    # agent_log.set_sync(True)
    # ure_logger().set_level("debug")
    ure_logger().set_level("info")
    # ure_logger().set_sync(True)
    miner_log = MinerLogger(atomspace)
    # miner_log.set_level("debug")
    miner_log.set_level("info")
    # miner_log.set_sync(True)

    # Delete log file of the previous run to have a clean log file for the current run

    try:
        if exists('opencog.log'):
            os.remove('opencog.log')
            while True:
                time.sleep(2)
                if not exists('opencog.log'):
                    break
            print('opencog.log has been deleted.')
        else:
            print('opencog.log doesnt exist and cant be deleted.')
    except:
        logging.exception('message')


    # Wrap environment
    wrapped_env = ChaseWrapper(env, atomspace)

    # ChaseAgent
    ca = ChaseAgent(wrapped_env, atomspace)

    # Training/learning loop
    lt_iterations = 2  # Number of learning-training iterations
    # lt_iterations = 1  # Number of learning-training iterations
    lt_period = 200  # Duration of a learning-training iteration
    # lt_period = 4  # Duration of a learning-training iteration
    for i in range(lt_iterations):
        print('lt_iterations = ',i)
        wrapped_env.restart()
        # print('calling reset_action_counter::::::::::::::::::::::')
        ca.reset_action_counter()
        # print('end calling reset_action_counter::::::::::::::::::::::')
        par = ca.accumulated_reward  # Keep track of the reward before
        # Discover patterns to make more informed decisions
        agent_log.info("Start learning ({}/{})".format(i + 1, lt_iterations))
        # print(time.strftime("%H:%M:%S", time.gmtime()))
        ca.learn()
        # print(time.strftime("%H:%M:%S", time.gmtime()))
        # Run agent to accumulate percepta
        agent_log.info("Start training ({}/{})".format(i + 1, lt_iterations))
        for j in range(lt_period):
            ca.control_cycle()
            wrapped_env.render()
            # print("lt_period=",j)
            time.sleep(0.1)
            # time.sleep(1)
            log.info("cycle_count = {}".format(ca.cycle_count))
        nar = ca.accumulated_reward - par
        agent_log.info(
            "Accumulated reward during {}th iteration = {}".format(i + 1, nar)
        )
        agent_log.info(
            "Action counter during {}th iteration:\n{}".format(i + 1, ca.action_counter)
        )

    # Get size of log file
    process = subprocess.Popen('du -sh opencog.log'.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print('Size of opencog.log is', output.decode("utf-8").split()[0])