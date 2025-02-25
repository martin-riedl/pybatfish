# coding=utf-8
#   Copyright 2018 The Batfish Open Source Project
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
import pytest

from pybatfish.client.session import Session


@pytest.fixture()
def session():
    return Session()


def test_get_component_versions(session):
    """Confirm component versions can be fetched from the service."""
    # Make sure Batfish is one of the versioned components
    assert 'Batfish' in session.get_component_versions()
