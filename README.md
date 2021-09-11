# Simple Ceph cluster health check for Nagios (no root)
API based ceph cluster health checker for nagios. Uses no root and needs the dashboard plugin on the mgr node.

Runs as a nagios plugin or an NRPE check. As long as the mgr node web dashboard is accessible.

## Output
Output consists of one line that is the cluster status. (ex: "HEALTH_OK")

## Alert condition
If "HEALTH_OK", return zero (OK), else return 1 (warning)

## Security
I have a read only dashboard account set up. The username and password are still in plain text so it is vulnerable to leakage. Can be run with NRPE to prevent the script from being visible to the nagios server.
