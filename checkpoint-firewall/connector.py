"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""
from connectors.core.connector import Connector, get_logger, ConnectorError
from .operation import CheckPointOps

logger = get_logger('checkpoint-firewall')


class CheckPoint(Connector):
    def execute(self, config, operation, params, **kwargs):
        config = config
        params = params
        connector_info = {"connector_name": self._info_json.get('name'),
                          "connector_version": self._info_json.get('version')}
        checkpoint = CheckPointOps(config, connector_info)
        checkpoint_operations = {
            'block_ip': checkpoint.block_ip,
            'block_applications': checkpoint.block_applications,
            'block_urls': checkpoint.block_urls,
            'unblock_ip': checkpoint.unblock_ip,
            'unblock_applications': checkpoint.unblock_applications,
            'unblock_urls': checkpoint.unblock_urls,
            'get_blocked_ip_addresses': checkpoint.get_blocked_ip_addresses,
            'get_blocked_urls': checkpoint.get_blocked_urls,
            'get_blocked_application_names': checkpoint.get_blocked_application_names,
            'get_list_of_applications': checkpoint.get_list_of_applications,
            'show_sessions': checkpoint.show_sessions,
            'discard_session': checkpoint.discard_session,
            'check_policies': checkpoint.check_policies,
            'get_session': checkpoint.get_session
        }
        logger.info('In execute() Operation:[{}]'.format(operation))
        operation = checkpoint_operations.get(operation, None)
        if not operation:
            logger.info('Unsupported operation [{}]'.format(operation))
            raise ConnectorError('Unsupported operation')
        result = operation(config, params)
        return result

    def check_health(self, config):
        connector_info = {"connector_name": self._info_json.get('name'),
                          "connector_version": self._info_json.get('version')}
        checkpoint = CheckPointOps(config, connector_info)
        return checkpoint.check_health()
