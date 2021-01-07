REQUEST_TIMEOUT=0.5
TIMEOUT_MULTIPLIER=2
MAX_TIMEOUT=60
MAX_ADDITIONAL_TIMEOUT=2
MIN_SECONDS_WITHOUT_PREDELAY=1
REQUEST_RETRIES=5
MAX_CACHED_QUERIES=1000000
MAX_CONCURRENT_REQUESTS=250
MAX_REQUESTS_PER_NAMESERVER_SECOND=100
MAX_REQUESTS_PER_TLD_NAMESERVER_SECOND=10000
MAX_RETURNED_RATELIMITER_STATS = 100
ROOT_SERVERS = {
    "a.root-servers.net": {"198.41.0.4"},
    # "b.root-servers.net": {"199.9.14.201"},
    # "c.root-servers.net": {"192.33.4.12"},
    # "d.root-servers.net": {"199.7.91.13"},
    # "e.root-servers.net": {"192.203.230.10"},
    # "f.root-servers.net": {"192.5.5.241"},
    # "g.root-servers.net": {"192.112.36.4"},
    # "h.root-servers.net": {"198.97.190.53"},
    # "i.root-servers.net": {"192.36.148.17"},
    # "j.root-servers.net": {"192.58.128.30"},
    # "k.root-servers.net": {"193.0.14.129"},
    # "l.root-servers.net": {"199.7.83.42"},
    # "m.root-servers.net": {"202.12.27.33}"
}
VALID_NODE_TRUST_TYPES = {'parent', 'child', 'provisioning'}
