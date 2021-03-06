#
# Copyright (C) 2012-2015 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


import gettext

from otopi import plugin, util

from ovirt_engine_extension_aaa_ldap_setup import constants


def _(m):
    return gettext.dgettext(
        message=m,
        domain='ovirt-engine-extension-aaa-ldap-setup',
    )


@util.export
class Plugin(plugin.PluginBase):

    MY_PROFILES = (
        {
            'display': _('389ds'),
            'profile': '389ds',
        },
        {
            'display': _('IPA'),
            'profile': 'ipa',
        },
        {
            'display': _('iPlanet'),
            'profile': 'iplanet',
        },
        {
            'display': _('OpenLDAP Standard Schema'),
            'profile': 'openldap',
        },
        {
            'display': _('RFC-2307 Schema (Generic)'),
            'profile': 'rfc2307-generic',
        },
        {
            'display': _('389ds RFC-2307 Schema'),
            'profile': 'rfc2307-389ds',
        },
        {
            'display': _('RHDS RFC-2307 Schema'),
            'profile': 'rfc2307-rhds',
        },
        {
            'display': _('Novell eDirectory RFC-2307 Schema'),
            'profile': 'rfc2307-edir',
        },
        {
            'display': _('OpenLDAP RFC-2307 Schema'),
            'profile': 'rfc2307-openldap',
        },
        {
            'display': _('Oracle Unified Directory RFC-2307 Schema'),
            'profile': 'rfc2307-openldap',
        },
        {
            'display': _('RHDS'),
            'profile': 'rhds',
        },
    )

    def __init__(self, context):
        super(Plugin, self).__init__(context=context)

    @plugin.event(
        stage=plugin.Stages.STAGE_INIT,
        after=(
            constants.Stages.LDAP_COMMON_INIT,
        ),
    )
    def _init(self):
        self.environment[
            constants.LDAPEnv.AVAILABLE_PROFILES
        ].extend(self.MY_PROFILES)


# vim: expandtab tabstop=4 shiftwidth=4
