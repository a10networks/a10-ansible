#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2021 A10 Networks
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")

DOCUMENTATION = r'''
module: a10_snmp_server_enable
description:
    - Enable SNMP service
author: A10 Networks 2021
options:
    state:
        description:
        - State of the object to be created.
        choices:
          - noop
          - present
          - absent
        type: str
        required: True
    ansible_host:
        description:
        - Host for AXAPI authentication
        type: str
        required: True
    ansible_username:
        description:
        - Username for AXAPI authentication
        type: str
        required: True
    ansible_password:
        description:
        - Password for AXAPI authentication
        type: str
        required: True
    ansible_port:
        description:
        - Port for AXAPI authentication
        type: int
        required: True
    a10_device_context_id:
        description:
        - Device ID for aVCS configuration
        choices: [1-8]
        type: int
        required: False
    a10_partition:
        description:
        - Destination/target partition for object/command
        type: str
        required: False
    service:
        description:
        - "Enable SNMP service"
        type: bool
        required: False
    uuid:
        description:
        - "uuid of the object"
        type: str
        required: False
    traps:
        description:
        - "Field traps"
        type: dict
        required: False
        suboptions:
            all:
                description:
                - "Enable all SNMP traps"
                type: bool
            lldp:
                description:
                - "Enable lldp traps"
                type: bool
            uuid:
                description:
                - "uuid of the object"
                type: str
            routing:
                description:
                - "Field routing"
                type: dict
            gslb:
                description:
                - "Field gslb"
                type: dict
            slb:
                description:
                - "Field slb"
                type: dict
            snmp:
                description:
                - "Field snmp"
                type: dict
            vrrp_a:
                description:
                - "Field vrrp_a"
                type: dict
            vcs:
                description:
                - "Field vcs"
                type: dict
            system:
                description:
                - "Field system"
                type: dict
            slb_change:
                description:
                - "Field slb_change"
                type: dict
            lsn:
                description:
                - "Field lsn"
                type: dict
            network:
                description:
                - "Field network"
                type: dict
            ssl:
                description:
                - "Field ssl"
                type: dict

'''

EXAMPLES = """
"""

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'supported_by': 'community',
    'status': ['preview']
}

# Hacky way of having access to object properties for evaluation
AVAILABLE_PROPERTIES = [
    "service",
    "traps",
    "uuid",
]

from ansible_collections.a10.acos_axapi.plugins.module_utils import \
    errors as a10_ex
from ansible_collections.a10.acos_axapi.plugins.module_utils.axapi_http import \
    client_factory
from ansible_collections.a10.acos_axapi.plugins.module_utils.kwbl import \
    KW_OUT, translate_blacklist as translateBlacklist


def get_default_argspec():
    return dict(
        ansible_host=dict(type='str', required=True),
        ansible_username=dict(type='str', required=True),
        ansible_password=dict(type='str', required=True, no_log=True),
        state=dict(type='str',
                   default="present",
                   choices=['noop', 'present', 'absent']),
        ansible_port=dict(type='int', choices=[80, 443], required=True),
        a10_partition=dict(
            type='dict',
            name=dict(type='str', ),
            shared=dict(type='str', ),
            required=False,
        ),
        a10_device_context_id=dict(
            type='int',
            choices=[1, 2, 3, 4, 5, 6, 7, 8],
            required=False,
        ),
        get_type=dict(type='str', choices=["single", "list", "oper", "stats"]),
    )


def get_argspec():
    rv = get_default_argspec()
    rv.update({
        'service': {
            'type': 'bool',
        },
        'uuid': {
            'type': 'str',
        },
        'traps': {
            'type': 'dict',
            'all': {
                'type': 'bool',
            },
            'lldp': {
                'type': 'bool',
            },
            'uuid': {
                'type': 'str',
            },
            'routing': {
                'type': 'dict',
                'bgp': {
                    'type': 'dict',
                    'bgpEstablishedNotification': {
                        'type': 'bool',
                    },
                    'bgpBackwardTransNotification': {
                        'type': 'bool',
                    },
                    'uuid': {
                        'type': 'str',
                    }
                },
                'isis': {
                    'type': 'dict',
                    'isisAdjacencyChange': {
                        'type': 'bool',
                    },
                    'isisAreaMismatch': {
                        'type': 'bool',
                    },
                    'isisAttemptToExceedMaxSequence': {
                        'type': 'bool',
                    },
                    'isisAuthenticationFailure': {
                        'type': 'bool',
                    },
                    'isisAuthenticationTypeFailure': {
                        'type': 'bool',
                    },
                    'isisCorruptedLSPDetected': {
                        'type': 'bool',
                    },
                    'isisDatabaseOverload': {
                        'type': 'bool',
                    },
                    'isisIDLenMismatch': {
                        'type': 'bool',
                    },
                    'isisLSPTooLargeToPropagate': {
                        'type': 'bool',
                    },
                    'isisManualAddressDrops': {
                        'type': 'bool',
                    },
                    'isisMaxAreaAddressesMismatch': {
                        'type': 'bool',
                    },
                    'isisOriginatingLSPBufferSizeMismatch': {
                        'type': 'bool',
                    },
                    'isisOwnLSPPurge': {
                        'type': 'bool',
                    },
                    'isisProtocolsSupportedMismatch': {
                        'type': 'bool',
                    },
                    'isisRejectedAdjacency': {
                        'type': 'bool',
                    },
                    'isisSequenceNumberSkip': {
                        'type': 'bool',
                    },
                    'isisVersionSkew': {
                        'type': 'bool',
                    },
                    'uuid': {
                        'type': 'str',
                    }
                },
                'ospf': {
                    'type': 'dict',
                    'ospfIfAuthFailure': {
                        'type': 'bool',
                    },
                    'ospfIfConfigError': {
                        'type': 'bool',
                    },
                    'ospfIfRxBadPacket': {
                        'type': 'bool',
                    },
                    'ospfIfStateChange': {
                        'type': 'bool',
                    },
                    'ospfLsdbApproachingOverflow': {
                        'type': 'bool',
                    },
                    'ospfLsdbOverflow': {
                        'type': 'bool',
                    },
                    'ospfMaxAgeLsa': {
                        'type': 'bool',
                    },
                    'ospfNbrStateChange': {
                        'type': 'bool',
                    },
                    'ospfOriginateLsa': {
                        'type': 'bool',
                    },
                    'ospfTxRetransmit': {
                        'type': 'bool',
                    },
                    'ospfVirtIfAuthFailure': {
                        'type': 'bool',
                    },
                    'ospfVirtIfConfigError': {
                        'type': 'bool',
                    },
                    'ospfVirtIfRxBadPacket': {
                        'type': 'bool',
                    },
                    'ospfVirtIfStateChange': {
                        'type': 'bool',
                    },
                    'ospfVirtIfTxRetransmit': {
                        'type': 'bool',
                    },
                    'ospfVirtNbrStateChange': {
                        'type': 'bool',
                    },
                    'uuid': {
                        'type': 'str',
                    }
                }
            },
            'gslb': {
                'type': 'dict',
                'all': {
                    'type': 'bool',
                },
                'zone': {
                    'type': 'bool',
                },
                'site': {
                    'type': 'bool',
                },
                'group': {
                    'type': 'bool',
                },
                'service_ip': {
                    'type': 'bool',
                },
                'uuid': {
                    'type': 'str',
                }
            },
            'slb': {
                'type': 'dict',
                'all': {
                    'type': 'bool',
                },
                'application_buffer_limit': {
                    'type': 'bool',
                },
                'gateway_up': {
                    'type': 'bool',
                },
                'gateway_down': {
                    'type': 'bool',
                },
                'server_conn_limit': {
                    'type': 'bool',
                },
                'server_conn_resume': {
                    'type': 'bool',
                },
                'server_up': {
                    'type': 'bool',
                },
                'server_down': {
                    'type': 'bool',
                },
                'server_disabled': {
                    'type': 'bool',
                },
                'server_selection_failure': {
                    'type': 'bool',
                },
                'service_conn_limit': {
                    'type': 'bool',
                },
                'service_conn_resume': {
                    'type': 'bool',
                },
                'service_down': {
                    'type': 'bool',
                },
                'service_up': {
                    'type': 'bool',
                },
                'service_group_up': {
                    'type': 'bool',
                },
                'service_group_down': {
                    'type': 'bool',
                },
                'service_group_member_up': {
                    'type': 'bool',
                },
                'service_group_member_down': {
                    'type': 'bool',
                },
                'vip_connlimit': {
                    'type': 'bool',
                },
                'vip_connratelimit': {
                    'type': 'bool',
                },
                'vip_down': {
                    'type': 'bool',
                },
                'vip_port_connlimit': {
                    'type': 'bool',
                },
                'vip_port_connratelimit': {
                    'type': 'bool',
                },
                'vip_port_down': {
                    'type': 'bool',
                },
                'vip_port_up': {
                    'type': 'bool',
                },
                'vip_up': {
                    'type': 'bool',
                },
                'bw_rate_limit_exceed': {
                    'type': 'bool',
                },
                'bw_rate_limit_resume': {
                    'type': 'bool',
                },
                'uuid': {
                    'type': 'str',
                }
            },
            'snmp': {
                'type': 'dict',
                'all': {
                    'type': 'bool',
                },
                'linkdown': {
                    'type': 'bool',
                },
                'linkup': {
                    'type': 'bool',
                },
                'uuid': {
                    'type': 'str',
                }
            },
            'vrrp_a': {
                'type': 'dict',
                'all': {
                    'type': 'bool',
                },
                'active': {
                    'type': 'bool',
                },
                'standby': {
                    'type': 'bool',
                },
                'uuid': {
                    'type': 'str',
                }
            },
            'vcs': {
                'type': 'dict',
                'state_change': {
                    'type': 'bool',
                },
                'uuid': {
                    'type': 'str',
                }
            },
            'system': {
                'type': 'dict',
                'all': {
                    'type': 'bool',
                },
                'control_cpu_high': {
                    'type': 'bool',
                },
                'data_cpu_high': {
                    'type': 'bool',
                },
                'fan': {
                    'type': 'bool',
                },
                'file_sys_read_only': {
                    'type': 'bool',
                },
                'high_disk_use': {
                    'type': 'bool',
                },
                'high_memory_use': {
                    'type': 'bool',
                },
                'high_temp': {
                    'type': 'bool',
                },
                'low_temp': {
                    'type': 'bool',
                },
                'license_management': {
                    'type': 'bool',
                },
                'packet_drop': {
                    'type': 'bool',
                },
                'power': {
                    'type': 'bool',
                },
                'pri_disk': {
                    'type': 'bool',
                },
                'restart': {
                    'type': 'bool',
                },
                'sec_disk': {
                    'type': 'bool',
                },
                'shutdown': {
                    'type': 'bool',
                },
                'smp_resource_event': {
                    'type': 'bool',
                },
                'syslog_severity_one': {
                    'type': 'bool',
                },
                'tacacs_server_up_down': {
                    'type': 'bool',
                },
                'start': {
                    'type': 'bool',
                },
                'uuid': {
                    'type': 'str',
                }
            },
            'slb_change': {
                'type': 'dict',
                'all': {
                    'type': 'bool',
                },
                'resource_usage_warning': {
                    'type': 'bool',
                },
                'connection_resource_event': {
                    'type': 'bool',
                },
                'server': {
                    'type': 'bool',
                },
                'server_port': {
                    'type': 'bool',
                },
                'ssl_cert_change': {
                    'type': 'bool',
                },
                'ssl_cert_expire': {
                    'type': 'bool',
                },
                'vip': {
                    'type': 'bool',
                },
                'vip_port': {
                    'type': 'bool',
                },
                'system_threshold': {
                    'type': 'bool',
                },
                'uuid': {
                    'type': 'str',
                }
            },
            'lsn': {
                'type': 'dict',
                'all': {
                    'type': 'bool',
                },
                'total_port_usage_threshold': {
                    'type': 'bool',
                },
                'per_ip_port_usage_threshold': {
                    'type': 'bool',
                },
                'max_port_threshold': {
                    'type': 'int',
                },
                'max_ipport_threshold': {
                    'type': 'int',
                },
                'fixed_nat_port_mapping_file_change': {
                    'type': 'bool',
                },
                'traffic_exceeded': {
                    'type': 'bool',
                },
                'uuid': {
                    'type': 'str',
                }
            },
            'network': {
                'type': 'dict',
                'trunk_port_threshold': {
                    'type': 'bool',
                },
                'uuid': {
                    'type': 'str',
                }
            },
            'ssl': {
                'type': 'dict',
                'server_certificate_error': {
                    'type': 'bool',
                },
                'uuid': {
                    'type': 'str',
                }
            }
        }
    })
    return rv


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/snmp-server/enable"

    f_dict = {}

    return url_base.format(**f_dict)


def list_url(module):
    """Return the URL for a list of resources"""
    ret = existing_url(module)
    return ret[0:ret.rfind('/')]


def get(module):
    return module.client.get(existing_url(module))


def get_list(module):
    return module.client.get(list_url(module))


def exists(module):
    try:
        return get(module)
    except a10_ex.NotFound:
        return None


def _to_axapi(key):
    return translateBlacklist(key, KW_OUT).replace("_", "-")


def _build_dict_from_param(param):
    rv = {}

    for k, v in param.items():
        hk = _to_axapi(k)
        if isinstance(v, dict):
            v_dict = _build_dict_from_param(v)
            rv[hk] = v_dict
        elif isinstance(v, list):
            nv = [_build_dict_from_param(x) for x in v]
            rv[hk] = nv
        else:
            rv[hk] = v

    return rv


def build_envelope(title, data):
    return {title: data}


def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/snmp-server/enable"

    f_dict = {}

    return url_base.format(**f_dict)


def validate(params):
    # Ensure that params contains all the keys.
    requires_one_of = sorted([])
    present_keys = sorted([
        x for x in requires_one_of if x in params and params.get(x) is not None
    ])

    errors = []
    marg = []

    if not len(requires_one_of):
        return REQUIRED_VALID

    if len(present_keys) == 0:
        rc, msg = REQUIRED_NOT_SET
        marg = requires_one_of
    elif requires_one_of == present_keys:
        rc, msg = REQUIRED_MUTEX
        marg = present_keys
    else:
        rc, msg = REQUIRED_VALID

    if not rc:
        errors.append(msg.format(", ".join(marg)))

    return rc, errors


def build_json(title, module):
    rv = {}

    for x in AVAILABLE_PROPERTIES:
        v = module.params.get(x)
        if v is not None:
            rx = _to_axapi(x)

            if isinstance(v, dict):
                nv = _build_dict_from_param(v)
                rv[rx] = nv
            elif isinstance(v, list):
                nv = [_build_dict_from_param(x) for x in v]
                rv[rx] = nv
            else:
                rv[rx] = module.params[x]

    return build_envelope(title, rv)


def report_changes(module, result, existing_config, payload):
    if existing_config:
        for k, v in payload["enable"].items():
            if isinstance(v, str):
                if v.lower() == "true":
                    v = 1
                else:
                    if v.lower() == "false":
                        v = 0
            elif k not in payload:
                break
            else:
                if existing_config["enable"][k] != v:
                    if result["changed"] is not True:
                        result["changed"] = True
                    existing_config["enable"][k] = v
            result.update(**existing_config)
    else:
        result.update(**payload)
    return result


def create(module, result, payload):
    try:
        post_result = module.client.post(new_url(module), payload)
        if post_result:
            result.update(**post_result)
        result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result


def update(module, result, existing_config, payload):
    try:
        post_result = module.client.post(existing_url(module), payload)
        if post_result:
            result.update(**post_result)
        if post_result == existing_config:
            result["changed"] = False
        else:
            result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result


def present(module, result, existing_config):
    payload = build_json("enable", module)
    changed_config = report_changes(module, result, existing_config, payload)
    if module.check_mode:
        return changed_config
    elif not existing_config:
        return create(module, result, payload)
    elif existing_config and not changed_config.get('changed'):
        return update(module, result, existing_config, payload)
    else:
        result["changed"] = True
        return result


def delete(module, result):
    try:
        module.client.delete(existing_url(module))
        result["changed"] = True
    except a10_ex.NotFound:
        result["changed"] = False
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result


def absent(module, result, existing_config):
    if module.check_mode:
        if existing_config:
            result["changed"] = True
            return result
        else:
            result["changed"] = False
            return result
    else:
        return delete(module, result)


def replace(module, result, existing_config, payload):
    try:
        post_result = module.client.put(existing_url(module), payload)
        if post_result:
            result.update(**post_result)
        if post_result == existing_config:
            result["changed"] = False
        else:
            result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result


def run_command(module):
    run_errors = []

    result = dict(changed=False, original_message="", message="", result={})

    state = module.params["state"]
    ansible_host = module.params["ansible_host"]
    ansible_username = module.params["ansible_username"]
    ansible_password = module.params["ansible_password"]
    ansible_port = module.params["ansible_port"]
    a10_partition = module.params["a10_partition"]
    a10_device_context_id = module.params["a10_device_context_id"]

    if ansible_port == 80:
        protocol = "http"
    elif ansible_port == 443:
        protocol = "https"

    valid = True

    if state == 'present':
        valid, validation_errors = validate(module.params)
        for ve in validation_errors:
            run_errors.append(ve)

    if not valid:
        err_msg = "\n".join(run_errors)
        result["messages"] = "Validation failure: " + str(run_errors)
        module.fail_json(msg=err_msg, **result)

    module.client = client_factory(ansible_host, ansible_port, protocol,
                                   ansible_username, ansible_password)

    if a10_partition:
        module.client.activate_partition(a10_partition)

    if a10_device_context_id:
        module.client.change_context(a10_device_context_id)

    existing_config = exists(module)

    if state == 'present':
        result = present(module, result, existing_config)

    if state == 'absent':
        result = absent(module, result, existing_config)

    if state == 'noop':
        if module.params.get("get_type") == "single":
            result["result"] = get(module)
        elif module.params.get("get_type") == "list":
            result["result"] = get_list(module)
    module.client.session.close()
    return result


def main():
    module = AnsibleModule(argument_spec=get_argspec(),
                           supports_check_mode=True)
    result = run_command(module)
    module.exit_json(**result)


# standard ansible module imports
from ansible.module_utils.basic import AnsibleModule

if __name__ == '__main__':
    main()
