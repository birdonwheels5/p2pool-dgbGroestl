from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    digibyteSha=math.Object(
        PARENT = networks.nets['digibyteSha']
        SHARE_PERIOD = 10 # seconds target spacing
        CHAIN_LENGTH = 12*60*60//10 # shares
        REAL_CHAIN_LENGTH = 12*60*60//10 # shares
        TARGET_LOOKBEHIND = 20 # shares diff regulation
        SPREAD = 50 # blocks
        IDENTIFIER = '48a4ebc31b798115'.decode('hex')
        PREFIX = '5685a276c2dd81db'.decode('hex')
        P2P_PORT = 8022
        MIN_TARGET = 0
        MAX_TARGET = 2**256//2**20 - 1
        PERSIST = False
        WORKER_PORT = 9022
        BOOTSTRAP_ADDRS = 'p2p.mine.bz pool2eu.dgbmining.com dgbpool.cloudapp.net pool2na.dgbmining.com pool2me.dgbmining.com p2pool-eu.gotgeeks.com p2pool-us.gotgeeks.com rav3n.dtdns.net doge.dtdns.net pool.hostv.pl p2pool.org p2pool.gotgeeks.com p2pool.dtdns.net solidpool.org taken.pl'.split(' ')
        ANNOUNCE_CHANNEL = '#p2pool-alt'
        VERSION_CHECK = lambda v: True
    ),
    digibyteSha_testnet=math.Object(
        PARENT = networks.nets['digibyteSha_testnet']
        SHARE_PERIOD = 10 # seconds target spacing
        CHAIN_LENGTH = 12*60*60//10 # shares
        REAL_CHAIN_LENGTH = 12*60*60//10 # shares
        TARGET_LOOKBEHIND = 20 # shares diff regulation
        SPREAD = 50 # blocks
        IDENTIFIER = '48a4ebc31b798115'.decode('hex')
        PREFIX = '5685a276c2dd81db'.decode('hex')
        P2P_PORT = 8022
        MIN_TARGET = 0
        MAX_TARGET = 2**256//2**20 - 1
        PERSIST = False
        WORKER_PORT = 9022
        BOOTSTRAP_ADDRS = 'p2p.mine.bz pool2eu.dgbmining.com dgbpool.cloudapp.net pool2na.dgbmining.com pool2me.dgbmining.com p2pool-eu.gotgeeks.com p2pool-us.gotgeeks.com rav3n.dtdns.net doge.dtdns.net pool.hostv.pl p2pool.org p2pool.gotgeeks.com p2pool.dtdns.net solidpool.org taken.pl'.split(' ')
        ANNOUNCE_CHANNEL = '#p2pool-alt'
        VERSION_CHECK = lambda v: True
    ),

)
for net_name, net in nets.iteritems():
    net.NAME = net_name
