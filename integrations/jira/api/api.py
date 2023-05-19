# region				-----External Imports-----
from django.conf import settings
import requests
import json
import typing
import utils
# endregion


class Jira(
        metaclass=utils.patterns.singleton.SingletonMeta
    ):
    account_id = settings.JIRA_OWNER_ID

    post_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    get_headers = {
        "Accept": "application/json"
    }

    def create_issue(self,
            description: typing.AnyStr,
            assignee_id: typing.AnyStr,
            project_id: typing.AnyStr,
            summary: typing.AnyStr,
            type: typing.AnyStr,

            parent_key: str = None
        ) -> typing.Dict:

        api_url = "https://neuraldynamics.atlassian"\
                  ".net/rest/api/2/issue"

        # ? Collect all appropriate parameters for request
        payload = {
            "fields": {
                "assignee": {"id": assignee_id},
                "project": {"id": project_id},
                "issuetype": {"name": type},
                "description": description,
                "summary": summary,
            }
        }

        # ? If parent key is set, then add to request
        if parent_key:
            payload["fields"]["parent"] = {
                "key": parent_key
            }
        
        payload = json.dumps(payload)
        
        response = requests.post(
            headers=self.post_headers,
            auth=self.auth,
            data=payload,
            url=api_url
        )

        # ? If not created successfuly raise error
        if response.status_code != 201:
            raise Exception(response.content)
        
        data = response.json()

        return data
    

    def get_project(self,
            key: typing.AnyStr
        ) -> typing.Dict:
        api_url = "https://neuraldynamics.atlassian"\
                  ".net/rest/api/3/project/{key}"\
                  .format(key=key)
        
        response = requests.get(
            headers=self.get_headers,
            auth=self.auth,
            url=api_url
        )

        data = response.json()

        return data


    def __init__(self,
            token: typing.AnyStr,
            email: typing.AnyStr
        ) -> None:
        self.auth = requests.auth\
            .HTTPBasicAuth(
                username=email,
                password=token
            )
        self.token = token
        self.email = email