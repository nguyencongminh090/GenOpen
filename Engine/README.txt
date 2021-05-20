##############################
------SUPPORTED-COMMANDS------
##############################

##############################
-------Gomocup-protocol-------
INFO
--------INFO max_memory 	// program requires at least 256MB of RAM memory to operate.
--------INFO max_memory 0	// specifying 0 means no memory limit, in such case the program will use 80% of total system memory.

START
--------START 15		// only board 15x15 is supported for standard rules.
--------START 20		// only board 20x20 is supported for freestyle rules.

RESTART
BEGIN
BOARD
TURN
TAKEBACK
END
ABOUT

##############################
--Gomocup-protocol-extension--
SWAP2BOARD

##############################
-----additional-commands------
PONDER - turns on pondering, can be used in two ways:
1-------PONDER 		// turns on infinite pondering.
2-------PONDER x	// turns on pondering for certain period of time (x in milliseconds).

STOP - stops current search and returns its result. 

SWAPBOARD - similar to SWAP2BOARD, for empty board returns 3-stone opening. If there are already 3 stones on board it either returns fourth move, or decides to swap colors.

##############################
---commands-send-by-program---
MESSAGE - after every turn program sends message summarizing the search results. For example 'MESSAGE depth 1-14 ev 56.2 n 3381 n/s 932 tm 3627 pv Oe4 Xe3 Of4 Xg4 Oh5 Xc3 Od3 Xf2 Oc5 Xg3 Og2 Xe1 Oh4 Xb2':
--------depth [x]-[y] is the minimal (x) and maximal (y) depth of the search (minimal is always 1)
--------ev [x] is the expectation outcome in % (alternatively can be interpreted as a probability of winning) or proven value - U (unknown), L (loss), D (draw), W (win)
--------n [x] is the number of evaluated nodes
--------n/s [x] is the number of evaluated nodes evaluated (including cache hits)
--------tm [x] is the time used for this turn (in milliseconds)
--------pv [list] is the principal variation, in piskvork format.
ERROR
UNKNOWN

##############################
--engine-initialization-info--
After START command program will send MESSAGE with detected devices, for example:
MESSAGE Detected following devices
MESSAGE CPU : GenuineIntel : 8 x AVX2 with 16252MB of memory
MESSAGE CUDA:0 : GeForce GTX 960M : 5 x SM 5.0 with 4096MB of memory
"CPU" or "CUDA:0" are names that have to be assigned in the "threads" section in the configuration file. If you don't see here a GPU (and you know have one) it means that you have something not installed correctly (most likely a driver). Currently only NVIDIA GPUs are supported.

##############################
Note that the engine cannot search infinitely, it will either run out of memory, or will reach maximum number of simulations (2^24 = 16777216).


##############################
------CONFIGURATION-FILE------
##############################

If you have no configuration file, program will generate new one on startup. Example configuration file looks like this.
{
  "use_logging": false, 			// if set to true, the engine will save some detailed info about search results into logfile. New file is created after every START or RESTART command.
  "always_ponder": false,			// if set to true, the engine will automatically turn on pondering mode after each move. In this mode, pondering can still be stopped using STOP command or then started again with another PONDER command.
  "swap2_openings_file": "swap2_openings.json",	// path to file with swap2 3-stone openings. If you look into that file, its structure will be self explaining.
  "networks": {
    "freestyle": "freestyle_6x64.bin",		// path to network used for freestyle rules.
    "standard": "standard_6x64.bin",		// path to network used for standard rule
    "renju": "",				// path to network used for renju rule (not supported yet, but added for future compatibility)
    "caro": ""					// path to network used for caro rule (not supported yet, but added for future compatibility)
  },
  "use_symmetries": true,			// if set to true, the engine will apply one of the possible symmetries (flips, rotations) to the board before sending it for neural network evaluation. Improves playing strength, but makes the search non-deterministic.
  "threads": [					// list of threads used by program, for each one a device must be assigned. The name of device can be taken from MESSAGE info sent by the engine after START command.
    {
      "device": "CPU"				// this thread uses one core of CPU for neural network evaluation
    },
    {
      "device": "CPU"				// this thread uses another core of the CPU for neural network evaluation
    }
  ],
  "search_options": {
    "batch_size": 8,				// how many positions each thread will evaluate in parallel. For CPU 8 or even 4 are usually enough to reach full efficiency, for GPU 32 or more could be used. Must be at least 1.
    "exploration_constant": 1.25,		// controls exploration in the search, the default value of 1.25 was found to give maximum playing strength.
    "expansion_prior_treshold": 0.0001,		// controls tree pruning, nodes that have lower prior policy (calculated by the network) will not be added to the tree. You can set this to 0.0 to disable pruning (will significantly increase memory consumption).
    "max_children": 30,				// controls tree pruning, after applying "expansion_prior_treshold" to prune low policy nodes, only "max_children" of best nodes will be added to the tree. You can set this to a number equal or larger than the board size (eg. 225 for 15x15 board) to disable pruning (will significantly increase memory consumption).
    "noise_weight": 0,				// parameter used only in the training, controls the amount of noise added at root node.
    "use_endgame_solver": true,			// if set to true, the engine will use endgame solver to prove win, draw or loss. Slightly increases playing strength, mostly saves time in the endgame, because the engine makes its moves much faster once they have been proven.
    "use_vcf_solver": true			// if set to true, the engine will use VCF solver.
  },
  "tree_options": {
    "max_number_of_nodes": 50000000,		// maximum number of nodes used in the tree. For long search times with GPU you can set this to much higher values eg. 500 millions of 1000 millions or so.
    "bucket_size": 100000			// nodes in the tree will be preallocated in buckets of this size. For long searches with GPU you can set this to eg. 1 million.
  },
  "cache_options": {
    "min_cache_size": 1048576,			// controls the size of a cache. You can set this to higher values but it should not significantly impact playing strength or speed.
    "max_cache_size": 1048576,			// currently unused, added for future possibility of automatic cache resize.
    "update_from_search": false,		// if set to true, the engine will update cached data with the search results. This feature turned out to be useless and will be removed in future versions.
    "update_visit_treshold": 1000		// controls treshold of how well explored the node needs to be to have its cache data updated from the search. This feature turned out to be useless and will be removed in future versions.
  }
}

For each supported rule there are two networks, small with name ending with "..._6x64.bin" or bigger "..._10x128.bin". If you have a GPU you should probably use the bigger one. On CPU you can experiment, the smaller might play better (because it's faster) but it's not always the case.

An example of "threads" section for GPU configuration could be:
"threads": [
    {
      "device": "CUDA:0"		// this thread uses NVIDIA GPU for neural network evaluation
    },
    {
      "device": "CUDA:0"		// this thread also uses NVIDIA GPU for neural network evaluation
    }
  ],
Typically two threads per each GPU should be enough to reach 100% efficiency (unless you have powerful GPU but poor CPU). And example of dual GPU setup could be:
"threads": [
    {
      "device": "CUDA:0"		// this thread uses the first NVIDIA GPU for neural network evaluation
    },
    {
      "device": "CUDA:0"		// this thread also uses the first NVIDIA GPU for neural network evaluation
    },
    {
      "device": "CUDA:1"		// this thread uses the second NVIDIA GPU for neural network evaluation
    },
    {
      "device": "CUDA:1"		// this thread also uses the second NVIDIA GPU for neural network evaluation
    }
  ],
In theory you can mix GPUs and CPU for different threads but it doesn't make sense.


########################
----LOGFILE-DETAILS-----
########################

In the logfile you can find all communication with the manager in lines starting with "Received : " and "Answered : ". Also you can find detailed info about search results, which can look like this:

########################
-----first-section------
Here you can see 10 best moves in the current position, sorted by their number of visits.
An example line can look like this:
CROSS  ( 7, 6) : W : Q=0.994799 : 0.000000 : 0.005201 : P=0.229409 : Visits=208 : Children=30

What does it mean?
"CROSS  ( 7, 6)" is sign, row and column of a move (point 0,0 is in upper left corner).
"W" is proven value, in this case it is a sure win. Most moves have "U" which means their proven value is unknown. Other values are "L" for loss, or "D" for draw.
"Q=0.994799 : 0.000000 : 0.005201" are three numbers, probability of win, draw and loss respectively.
"P=0.229409" is prior policy assigned by the network when this position was added to the tree. It represents the probability that this move is the best one in this position (at least that is what neural network thinks about this move).
"Visits=208" is the number of MCTS playouts that went through this node.
"Children=30" is the number of children in the tree for this node.

BEST
CROSS  ( 9, 5) : U : Q=0.982966 : 0.000009 : 0.017025 : P=0.326198 : Visits=1508 : Children=14
CROSS  ( 5, 6) : U : Q=0.912775 : 0.000046 : 0.087179 : P=0.310499 : Visits=215 : Children=1
CROSS  ( 7, 5) : U : Q=0.913119 : 0.000024 : 0.086856 : P=0.287416 : Visits=199 : Children=1
CROSS  ( 6, 9) : U : Q=0.835638 : 0.000176 : 0.164187 : P=0.037664 : Visits=13 : Children=1
CROSS  ( 4, 9) : U : Q=0.882123 : 0.000104 : 0.117773 : P=0.019546 : Visits=9 : Children=1
CROSS  ( 7, 6) : U : Q=0.821467 : 0.000043 : 0.178490 : P=0.013589 : Visits=4 : Children=1
CROSS  ( 4, 5) : U : Q=0.487948 : 0.000160 : 0.511892 : P=0.000621 : Visits=1 : Children=1
CROSS  (12, 5) : U : Q=0.000000 : 0.000000 : 0.000000 : P=0.000310 : Visits=0 : Children=0
CROSS  ( 8, 4) : U : Q=0.000000 : 0.000000 : 0.000000 : P=0.000062 : Visits=0 : Children=0
CROSS  ( 9,12) : U : Q=0.000000 : 0.000000 : 0.000000 : P=0.000062 : Visits=0 : Children=0


########################
-----second-section-----
Here you can find distribution of MCTS playouts over the board. For example a value of '772' means 77.2% of playouts went through this move. Sometimes, some positions will be marked with ">W<" or ">L<" or ">D<" which means that this move was proven to be win or loss or draw, respectively. Percentages lower than 0.1% are not shown at all. The values may not sum up to 100% and this is ok.
  _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _ 
  _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _ 
  _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _ 
  _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _ 
  _   _   _   _   _   _   _   _   _    4  _   _   _   _   _   _   _   _   _   _ 
  _   _   _   _   _   _  110  _   _   X   _   _   _   _   _   _   _   _   _   _ 
  _   _   _   _   _   _   _   X   _    6  _   _   _   _   _   _   _   _   _   _ 
  _   _   _   _   _  101   2  X   X   X   O   _   _   O   _   _   _   _   _   _ 
  _   _   _   _   _   O  >L<  O   O   X   _   X   O   X   _   _   _   _   _   _ 
  _   _   _   _   X  772  X   O   X   O   O  >L<  _   O   _   _   _   _   _   _ 
  _   _   _   _   X   O   O   O   X   O   X   _   _   X   _   _   _   _   _   _ 
  _   _   _   _   O   O   X   _   O   _   O   _   _   X   _   _   _   _   _   _ 
  _   _   _   _   X   _   O   X   _   _   X   _   _   O   _   _   _   _   _   _ 
  _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _ 
  _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _ 
  _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _ 
  _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _ 
  _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _ 
  _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _ 
  _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _ 

########################
-----third-section------
Here you can see pricipal variation.
CIRCLE ( 0, 0) : U : Q=0.034901 : 0.000016 : 0.965083 : P=0.000000 : Visits=1952 : Children=12
CROSS  ( 9, 5) : U : Q=0.982966 : 0.000009 : 0.017025 : P=0.326198 : Visits=1508 : Children=14
CIRCLE ( 8, 6) : U : Q=0.018029 : 0.000009 : 0.981961 : P=0.819632 : Visits=1397 : Children=1
CROSS  ( 8, 4) : U : Q=0.981996 : 0.000009 : 0.017995 : P=1.000000 : Visits=1396 : Children=30
CIRCLE ( 7, 5) : U : Q=0.020884 : 0.000011 : 0.979106 : P=0.094506 : Visits=1163 : Children=30
CROSS  ( 5, 7) : U : Q=0.993467 : 0.000007 : 0.006527 : P=0.157543 : Visits=260 : Children=30
CIRCLE ( 6, 4) : U : Q=0.006534 : 0.000007 : 0.993460 : P=0.334060 : Visits=109 : Children=1
CROSS  ( 5, 3) : U : Q=0.993467 : 0.000007 : 0.006527 : P=1.000000 : Visits=108 : Children=30
CIRCLE ( 4, 5) : U : Q=0.011293 : 0.000011 : 0.988696 : P=0.250715 : Visits=36 : Children=30
CROSS  ( 9,11) : U : Q=0.996134 : 0.000005 : 0.003861 : P=0.217192 : Visits=11 : Children=11
CIRCLE ( 8,10) : U : Q=0.002999 : 0.000008 : 0.996994 : P=0.270046 : Visits=5 : Children=30
CROSS  ( 5,10) : U : Q=0.999329 : 0.000001 : 0.000671 : P=0.304365 : Visits=2 : Children=11
CIRCLE ( 5, 5) : U : Q=0.000000 : 0.000000 : 0.000000 : P=0.134327 : Visits=0 : Children=0

########################
-----fourth-section-----
Here you can find the timing of various stages of the search. Typically they have following format: "name" : total time : number of events : average time of each event. On Windows the clock resolution is sometimes too low to capture most of the events, this is why you see 0.0s in the time sections.

----EvaluationQueue----
avg batch size = 7.980615				// this is the average number of positions evaluated by the neural network in each step. It should be close to the "batch_size" parameter in the config. If it isn't, then you probably use too large batch size.
network   = 34.033073s : 1496 : 22.749381 ms		// this is the time of each neural network evaluation
pack      = 0.000000s : 1496 : 0.000000 us		// this is the time of packing the data to network input		
unpack    = 0.000000s : 1496 : 0.000000 us		// this is the time of unpacking the data from network output

----SearchStats----
nb_duplicate_nodes = 0					// it can happen that the same node will be evaluated more than once (it is ok). This is the number of such nodes.
select     = 0.000000s : 1952 : 0.000000 us		// time of selection phase in MCTS
expand     = 0.000000s : 1952 : 0.000000 us		// time of tree expansion phase in MCTS
vcf solver = 0.281471s : 1952 : 144.196460 us		// time used by VCF solver
backup     = 0.000000s : 1952 : 0.000000 us		// time of backup phase in MCTS
evaluate   = 0.000000s : 1008 : 0.000000 us		// time of applying neural network evaluation results to the tree
game rules = 0.000000s : 1952 : 0.000000 us		// time of checking game rules to determine if the game ended or not

----TreeStats----
used nodes      = 17912					// number of node used in the tree
allocated nodes = 200000				// number of allocated nodes in the tree
proven nodes    = 14 : 0 : 1363 (win:draw:loss)		// number of proven nodes, with win, draw and loss respectively. When using VCF solver, most of the nodes will be proven as loss.
memory = 6MB						// memory used by the tree
----CacheStats----
hit rate = 48.300000%					// cache hit rate
time_seek    = 0.000000s : 1952 : 0.000000 us		// time of lookup to the cache
time_insert  = 0.000000s : 1008 : 0.000000 us		// time of inserton of new entry to the cache
time_cleanup = 0.015644s : 1 : 15.644312 ms		// time of cache cleanup (removing positions that will never appear again given the current board state)
entries = 1608 : 1754 : 3362 (stored:buffered:allocated)// number of entries in the cache, currently stored, buffered (allocated but not used currently) and overall allocated entries.
memory = 10MB						// memory used by the cache
