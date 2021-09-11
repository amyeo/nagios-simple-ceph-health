# Simple Ceph cluster health check for Nagios (no root)
API based ceph cluster health checker for nagios. Uses no root and needs the dashboard plugin on the mgr node.

Runs as a nagios plugin or an NRPE check. As long as the mgr node web dashboard is accessible.

## Output
Output consists of one line that is the cluster status. (ex: "HEALTH_OK")

## Alert condition
If "HEALTH_OK", return zero (OK), else return 1 (warning)
