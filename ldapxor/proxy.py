from twisted.internet import protocol
from twisted.internet import reactor
from twisted.python import log

from ldaptor.protocols.ldap.proxy import Proxy
from ldaptor.protocols.pureldap import LDAPSearchResultEntry
from ldaptor.protocols import pureldap
from ldaptor.config import LDAPConfig
import sys

log.startLogging(sys.stderr)


def rewriter(attr):

    if attr[0] == 'USERPRINCIPALNAME':

        attr_new = ['USERPRINCIPALNAME', []]
        for attrval in attr[1]:
            attr_new[1].append('CHEF!')

        return tuple(attr_new)
    else:
        return attr


class RewritingProxy(Proxy):

    def _gotResponse(self, response, reply):
        #print(
        #    "Returning resp to original client:\n{}".format(
        #        response
        #    )
        #)
        if isinstance(response, LDAPSearchResultEntry):
            # do some shitte with response before sending out :)
            if response.objectName == 'cn=SOMEONE,ou=Users,' \
                                      'dc=SOMEDC,dc=something,dc=com':
                attributes = []
                for attr in response.attributes:
                    attributes.append(rewriter(attr))

                response.attributes = attributes

        reply(response)

        # TODO this is ugly
        return isinstance(
            response, (
                pureldap.LDAPSearchResultDone,
                pureldap.LDAPBindResponse,
            )
        )

factory = protocol.ServerFactory()
config = LDAPConfig(serviceLocationOverrides={'': ('someldap.com', 389), })
factory.protocol = lambda: RewritingProxy(config=config)
reactor.listenTCP(10389, factory)
reactor.run()
