#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2018 A10 Networks
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")


DOCUMENTATION = r'''
module: a10_router_bgp_address_family_ipv6_neighbor_ipv4_neighbor
description:
    - Specify a peer-group neighbor router
short_description: Configures A10 router.bgp.address.family.ipv6.neighbor.ipv4-neighbor
author: A10 Networks 2018 
version_added: 2.4
options:
    state:
        description:
        - State of the object to be created.
        choices:
          - noop
          - present
        required: True
    a10_host:
        description:
        - Host for AXAPI authentication
        required: True
    a10_username:
        description:
        - Username for AXAPI authentication
        required: True
    a10_password:
        description:
        - Password for AXAPI authentication
        required: True
    a10_port:
        description:
        - Port for AXAPI authentication
        required: True
    a10_protocol:
        description:
        - Protocol for AXAPI authentication
        required: True
    a10_device_context_id:
        description:
        - Device ID for aVCS configuration
        choices: [1-8]
        required: False
    a10_partition:
        description:
        - Destination/target partition for object/command
        required: False
    bgp_as_number:
        description:
        - Key to identify parent object
    maximum_prefix:
        description:
        - "Maximum number of prefix accept from this peer (maximum no. of prefix limit (various depends on model))"
        required: False
    neighbor_prefix_lists:
        description:
        - "Field neighbor_prefix_lists"
        required: False
        suboptions:
            nbr_prefix_list_direction:
                description:
                - "'in'= in; 'out'= out; "
            nbr_prefix_list:
                description:
                - "Filter updates to/from this neighbor (Name of a prefix list)"
    allowas_in_count:
        description:
        - "Number of occurrences of AS number"
        required: False
    peer_group_name:
        description:
        - "Configure peer-group (peer-group name)"
        required: False
    send_community_val:
        description:
        - "'both'= Send Standard and Extended Community attributes; 'none'= Disable Sending Community attributes; 'standard'= Send Standard Community attributes; 'extended'= Send Extended Community attributes; "
        required: False
    neighbor_ipv4:
        description:
        - "Neighbor address"
        required: True
    inbound:
        description:
        - "Allow inbound soft reconfiguration for this neighbor"
        required: False
    next_hop_self:
        description:
        - "Disable the next hop calculation for this neighbor"
        required: False
    maximum_prefix_thres:
        description:
        - "threshold-value, 1 to 100 percent"
        required: False
    route_map:
        description:
        - "Route-map to specify criteria to originate default (route-map name)"
        required: False
    uuid:
        description:
        - "uuid of the object"
        required: False
    weight:
        description:
        - "Set default weight for routes from this neighbor"
        required: False
    unsuppress_map:
        description:
        - "Route-map to selectively unsuppress suppressed routes (Name of route map)"
        required: False
    default_originate:
        description:
        - "Originate default route to this neighbor"
        required: False
    activate:
        description:
        - "Enable the Address Family for this Neighbor"
        required: False
    remove_private_as:
        description:
        - "Remove private AS number from outbound updates"
        required: False
    prefix_list_direction:
        description:
        - "'both'= both; 'receive'= receive; 'send'= send; "
        required: False
    allowas_in:
        description:
        - "Accept as-path with my AS present in it"
        required: False
    neighbor_route_map_lists:
        description:
        - "Field neighbor_route_map_lists"
        required: False
        suboptions:
            nbr_rmap_direction:
                description:
                - "'in'= in; 'out'= out; "
            nbr_route_map:
                description:
                - "Apply route map to neighbor (Name of route map)"
    neighbor_filter_lists:
        description:
        - "Field neighbor_filter_lists"
        required: False
        suboptions:
            filter_list:
                description:
                - "Establish BGP filters (AS path access-list name)"
            filter_list_direction:
                description:
                - "'in'= in; 'out'= out; "
    distribute_lists:
        description:
        - "Field distribute_lists"
        required: False
        suboptions:
            distribute_list_direction:
                description:
                - "'in'= in; 'out'= out; "
            distribute_list:
                description:
                - "Filter updates to/from this neighbor (IP standard/extended/named access list)"


'''

EXAMPLES = """
"""

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'supported_by': 'community',
    'status': ['preview']
}

# Hacky way of having access to object properties for evaluation
AVAILABLE_PROPERTIES = ["activate","allowas_in","allowas_in_count","default_originate","distribute_lists","inbound","maximum_prefix","maximum_prefix_thres","neighbor_filter_lists","neighbor_ipv4","neighbor_prefix_lists","neighbor_route_map_lists","next_hop_self","peer_group_name","prefix_list_direction","remove_private_as","route_map","send_community_val","unsuppress_map","uuid","weight",]

# our imports go at the top so we fail fast.
try:
    from ansible_collections.a10.acos_axapi.plugins.module_utils import errors as a10_ex
    from ansible_collections.a10.acos_axapi.plugins.module_utils.axapi_http import client_factory, session_factory
    from ansible_collections.a10.acos_axapi.plugins.module_utils.kwbl import KW_IN, KW_OUT, translate_blacklist as translateBlacklist

except (ImportError) as ex:
    module.fail_json(msg="Import Error:{0}".format(ex))
except (Exception) as ex:
    module.fail_json(msg="General Exception in Ansible module import:{0}".format(ex))


def get_default_argspec():
    return dict(
        a10_host=dict(type='str', required=True),
        a10_username=dict(type='str', required=True),
        a10_password=dict(type='str', required=True, no_log=True),
        state=dict(type='str', default="present", choices=['noop', 'present']),
        a10_port=dict(type='int', required=True),
        a10_protocol=dict(type='str', choices=["http", "https"]),
        a10_partition=dict(type='dict', name=dict(type='str',), shared=dict(type='str',), required=False, ),
        a10_device_context_id=dict(type='int', choices=[1, 2, 3, 4, 5, 6, 7, 8], required=False, ),
        get_type=dict(type='str', choices=["single", "list", "oper", "stats"]),
    )

def get_argspec():
    rv = get_default_argspec()
    rv.update(dict(
        maximum_prefix=dict(type='int', ),
        neighbor_prefix_lists=dict(type='list', nbr_prefix_list_direction=dict(type='str', choices=['in', 'out']), nbr_prefix_list=dict(type='str', )),
        allowas_in_count=dict(type='int', ),
        peer_group_name=dict(type='str', ),
        send_community_val=dict(type='str', choices=['both', 'none', 'standard', 'extended']),
        neighbor_ipv4=dict(type='str', required=True, ),
        inbound=dict(type='bool', ),
        next_hop_self=dict(type='bool', ),
        maximum_prefix_thres=dict(type='int', ),
        route_map=dict(type='str', ),
        uuid=dict(type='str', ),
        weight=dict(type='int', ),
        unsuppress_map=dict(type='str', ),
        default_originate=dict(type='bool', ),
        activate=dict(type='bool', ),
        remove_private_as=dict(type='bool', ),
        prefix_list_direction=dict(type='str', choices=['both', 'receive', 'send']),
        allowas_in=dict(type='bool', ),
        neighbor_route_map_lists=dict(type='list', nbr_rmap_direction=dict(type='str', choices=['in', 'out']), nbr_route_map=dict(type='str', )),
        neighbor_filter_lists=dict(type='list', filter_list=dict(type='str', ), filter_list_direction=dict(type='str', choices=['in', 'out'])),
        distribute_lists=dict(type='list', distribute_list_direction=dict(type='str', choices=['in', 'out']), distribute_list=dict(type='str', ))
    ))
   
    # Parent keys
    rv.update(dict(
        bgp_as_number=dict(type='str', required=True),
    ))

    return rv

def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/router/bgp/{bgp_as_number}/address-family/ipv6/neighbor/ipv4-neighbor/{neighbor-ipv4}"

    f_dict = {}
    f_dict["neighbor-ipv4"] = module.params["neighbor_ipv4"]
    f_dict["bgp_as_number"] = module.params["bgp_as_number"]

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

    for k,v in param.items():
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
    return {
        title: data
    }

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/router/bgp/{bgp_as_number}/address-family/ipv6/neighbor/ipv4-neighbor/{neighbor-ipv4}"

    f_dict = {}
    f_dict["neighbor-ipv4"] = ""
    f_dict["bgp_as_number"] = module.params["bgp_as_number"]

    return url_base.format(**f_dict)

def validate(params):
    # Ensure that params contains all the keys.
    requires_one_of = sorted([])
    present_keys = sorted([x for x in requires_one_of if x in params and params.get(x) is not None])
    
    errors = []
    marg = []
    
    if not len(requires_one_of):
        return REQUIRED_VALID

    if len(present_keys) == 0:
        rc,msg = REQUIRED_NOT_SET
        marg = requires_one_of
    elif requires_one_of == present_keys:
        rc,msg = REQUIRED_MUTEX
        marg = present_keys
    else:
        rc,msg = REQUIRED_VALID
    
    if not rc:
        errors.append(msg.format(", ".join(marg)))
    
    return rc,errors

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
        for k, v in payload["ipv4-neighbor"].items():
            if isinstance(v, str):
                if v.lower() == "true":
                    v = 1
                else:
                    if v.lower() == "false":
                        v = 0
            elif k not in payload:
               break
            else:
                if existing_config["ipv4-neighbor"][k] != v:
                    if result["changed"] != True:
                        result["changed"] = True
                    existing_config["ipv4-neighbor"][k] = v
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
    payload = build_json("ipv4-neighbor", module)
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

    result = dict(
        changed=False,
        original_message="",
        message="",
        result={}
    )

    state = module.params["state"]
    a10_host = module.params["a10_host"]
    a10_username = module.params["a10_username"]
    a10_password = module.params["a10_password"]
    a10_port = module.params["a10_port"] 
    a10_protocol = module.params["a10_protocol"]
    a10_partition = module.params["a10_partition"]
    a10_device_context_id = module.params["a10_device_context_id"]

    valid = True

    if state == 'present':
        valid, validation_errors = validate(module.params)
        for ve in validation_errors:
            run_errors.append(ve)
    
    if not valid:
        err_msg = "\n".join(run_errors)
        result["messages"] = "Validation failure: " + str(run_errors)
        module.fail_json(msg=err_msg, **result)

    module.client = client_factory(a10_host, a10_port, a10_protocol, a10_username, a10_password)
    
    if a10_partition:
        module.client.activate_partition(a10_partition)

    if a10_device_context_id:
        module.client.change_context(a10_device_context_id)

    existing_config = exists(module)
    
    if state == 'present':
        result = present(module, result, existing_config)

    elif state == 'noop':
        if module.params.get("get_type") == "single":
            result["result"] = get(module)
        elif module.params.get("get_type") == "list":
            result["result"] = get_list(module)
    module.client.session.close()
    return result

def main():
    module = AnsibleModule(argument_spec=get_argspec(), supports_check_mode=True)
    result = run_command(module)
    module.exit_json(**result)

# standard ansible module imports
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *

if __name__ == '__main__':
    main()