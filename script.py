import logging
import requests as requests

REST_PROXY_URL = "http://localhost:8082/v3"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}


def get_result(topic_resp):
    if topic_resp.status_code == 201 or topic_resp.status_code == 200:
        return "successfully"
    return "failed"


def get_cluster_id():
    cluster_resp = requests.get(url=f'{REST_PROXY_URL}/clusters')
    return cluster_resp.json().get("data")[0].get("cluster_id")


def create_topic(topic):
    cluster = get_cluster_id()
    topic_resp = requests.post(url=f'{REST_PROXY_URL}/clusters/{cluster}/topics', headers=HEADERS, json={
        "topic_name": "test",
        "partitions_count": 1,
        "replication_factor": 1,
        "configs": [
            {
                "name": "cleanup.policy",
                "value": "delete"           # default value
            }
        ]
    })
    print(f'Creating topic: {topic} -> {get_result(topic_resp)}')


if __name__ == '__main__':
    create_topic('test')