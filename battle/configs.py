# coding: utf-8

IMG_SHAPE = (80, 80)
a_size = 3
model_path = './check_point/D3_battle/'
model_file = 'model-7400.ckpt'
# model_file = 'model-8700.ckpt'

SCENARIO_PATH = '../scenarios/D3_battle.cfg'

IS_SUPREME_VERSION = True
IS_TRAIN = False
AGENTS_NUM = 16

HIST_LEN = 4


def button_combinations():
    actions = []
    m_forward = [[True], [False]]  # move forward
    m_right_left = [[True, False], [False, True], [False, False], [True, True]]  # move right and move left
    t_right_left = [[True, False], [False, True], [False, False], [True, True]]  # turn right and turn left
    attack = [[True], [False]]
    speed = [[True], [False]]

    for i in m_forward:
        for j in m_right_left:
            for k in t_right_left:
                for m in attack:
                    for n in speed:
                        actions.append(i+j+k+m+n)
    return actions

ACTION_DIM = len(button_combinations())
SKIP_FRAME_NUM = 4

AGENT_PREFIX = 'Agent_'
AGENT_MONITOR = AGENT_PREFIX + '0'


IMITATION_DATA_DIR = '../record/data'
IMITATION_DATA_PATH = IMITATION_DATA_DIR + '/record_%s.pickle'
