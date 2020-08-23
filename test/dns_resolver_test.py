import sys
sys.path.append("../")
from dnscrawler import DNSResolver
from dnscrawler.logger import log
import json

if __name__ == "__main__":
    resolver = DNSResolver()
    domain_dict = resolver.get_domain_dict("ns2.wpx.ne.jp")
    print(json.dumps(domain_dict))

