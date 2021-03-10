from enum import Enum


class QuartersRelation(Enum):
    THE_SAME_QUARTER = 0
    OPPOSITE_QUARTERS = 1
    NEIGHBOR_QUARTERS = 2


class MenhirToCentreDistance(Enum):
    CLOSE = 0
    MODERATE = 1
    FAR = 2


class Actions(Enum):
    HIDE_IN_THE_STARTING_QUARTER = 0
    HIDE_IN_THE_OPPOSITE_QUARTER = 1
    HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL = 2
    HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL = 3


MODEL = {
    'fisher_island': {
        'Q': {((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 0.22992467128922234,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): 0.17943026671640966,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): -0.12344208574142904,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): 0.0,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 0.4548989420548715,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): 0.02103502882659619,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): 0.3702921504320579,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): -0.10757540447726575,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 0.7313031476277478,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): 0.6580391834518394,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): -0.14224624212916864,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): -0.028065866208010062,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): -0.09545150395459656,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): 0.16179405322112575,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): 0.0,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): 0.3668970409368541,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 0.154680470399934,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): -0.12987626417789752,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): 0.2444070461574085,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): -0.12011197855381334,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 0.8488181419593238,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): 0.9650877063229828,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): 0.2759985898098093,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): 0.0,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 0.5784709685121906,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): 0.646632046164722,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): 0.058595994943713314,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): -0.372047153261825,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 0.5556940456502864,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): 0.16334350706326567,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): 0.4008636427382529,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): 0.0,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_STARTING_QUARTER): -0.21762504445889094,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): 0.7298057687791627,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): 0.18892947184153952,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): 0.2910239359270998},
        'state': None, 'action': None, 'reward': None, 'reward_sum': 0,
        'attempt_no': 0, 'alpha': 0.0, 'epsilon': 0.0,
        'discount_factor': 0.0
    },
    'archipelago': {
        'Q': {((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 0.995834307141582,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): 0.05232102217090029,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): -0.29597419134528213,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): -0.2958972377958855,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 0.1531364188768764,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): -0.09865826788238026,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): -0.12326347442552091,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): 0.0,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 0.6481071134155268,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): -0.09742688981271574,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): -0.7113239982988857,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): -0.6373155275150763,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 0.4296449235907625,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): 0.0,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): -0.08500248519214545,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): -0.32960496095982594,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 0.6502105302838014,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): -0.16430443313605758,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): 0.0032762122030403785,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): -0.35423776701378007,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 0.5047725689294363,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): -0.07493915620797528,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): 0.1612891880502164,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): -0.5208984582537529,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 0.47145666289113575,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): -0.8723371161770824,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): -0.25982503707457894,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): -0.1609896266379855,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 0.6083425977820619,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): -0.044468350163312596,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): -0.4804952248051652,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): 0.03566753482889892,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 0.22812928009502365,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): -0.5226384736121703,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): 0.11150523655738054,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): -0.2681947048152571},
        'state': None, 'action': None, 'reward': None, 'reward_sum': 0,
        'attempt_no': 0, 'alpha': 0.0, 'epsilon': 0.0,
        'discount_factor': 0.0, 'reward_history': []
    },
    'wasteland': {
        'Q': {((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 1.8393556299159488,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): 0.0,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): 0.7162707723539665,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): 0.0,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 1.9760176513027974,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): 0.23562661701468307,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): 0.0,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): -0.007651578056932439,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 1.8363343816012967,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): -0.9600678814351844,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): 0.40163480392896356,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): 0.0,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 1.6104495448382947,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): 0.0,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): 0.4442148265331625,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): 0.34812812274296456,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 1.2176783199387091,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): -0.0777567836148454,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): 0.045725654172545954,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): 0.0,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 2.28233003222858,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): 0.0,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): 0.0,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): 0.3738183617026326,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 2.8984497003602345,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): 0.06727789002289068,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): 0.0,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): 0.0,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 1.2756655930841172,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): 0.3476856666039545,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): 0.35884189753363344,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): 0.1986994000248176,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 2.625773471685135,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): 0.5449941910203172,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): 1.1990896259754038,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): 0.2098319015387361},
        'state': None, 'action': None, 'reward': None, 'reward_sum': 0,
        'attempt_no': 0, 'alpha': 0.0, 'epsilon': 0.0,
        'discount_factor': 0.0,
    },
    'dungeon': {
        'Q': {((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): -0.04946532898731858,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): -0.24351655088959276,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): -0.05005289967478158,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): -0.07049055742942718,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 1.0195233937151669,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): 0.5813770656312719,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): 0.0,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): -0.13928264360991469,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 0.25095571139135847,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): -0.8407026653390162,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): -0.245090456877036,
              ((QuartersRelation.THE_SAME_QUARTER, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): 0.03371931941430905,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 0.2422449597176585,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): 0.12251807303635434,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): 0.0,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): -0.2875776702953904,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 1.022690578150419,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): 0.31701084746930186,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): 0.0,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): 0.23407268927847294,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_STARTING_QUARTER): -0.2020391209354672,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): 0.49118583050297915,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): -0.2093421979247877,
              ((QuartersRelation.OPPOSITE_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): -0.091808792798424,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 0.5522794639321243,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): 0.10504586716948948,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): 0.11085692119416107,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.CLOSE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): -0.05329205612797505,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 1.1136613700298923,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): -0.12482460932999537,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): -0.08439814567106926,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.MODERATE),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): 0.613409013905095,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_STARTING_QUARTER): 0.6155853659686903,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_OPPOSITE_QUARTER): 0.4798207994979128,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_HORIZONTAL): -0.14359313244228766,
              ((QuartersRelation.NEIGHBOR_QUARTERS, MenhirToCentreDistance.FAR),
               Actions.HIDE_IN_THE_NEIGHBOR_QUARTER_VERTICAL): 0.15232989387002427},
        'state': None, 'action': None, 'reward': None, 'reward_sum': 0,
        'attempt_no': 0, 'alpha': 0.0, 'epsilon': 0.0,
        'discount_factor': 0.0},
}
