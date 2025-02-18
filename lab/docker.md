# Configuration Docker

/etc/docker/daemon.json

```json
{
  "data-root": "/new/path/to/docker-data",
  "default-address-pools": [
    {
      "base": "172.80.0.0/16",
      "size": 24
    },
    {
      "base": "192.170.0.0/16",
      "size": 24
    }
  ]
}
```