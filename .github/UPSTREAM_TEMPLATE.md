<!--- Verify first that your issue/request is not already reported in GitHub -->

##### ISSUE TYPE
<!--- Pick one below and delete the rest: -->
 - Upstream request

##### COMPONENT NAME
<!--- Name of the module/role/task -->

##### ANSIBLE VERSION
<!--- Paste verbatim output from “ansible --version” between quotes below -->
```

```

##### PYTHON VERSION
<!--- Paste verbatim output from “python -V” between quotes below -->
```

```

##### BIGIP VERSION
<!---
Paste a list of BIG-IP versions this was tested on.
This is usually reflected in the playbook that runs the functional test.

Check the tested versions
-->
- [ ] 12.0.0 (BIGIP-12.0.0.0.0.606)
- [ ] 12.1.0 (BIGIP-12.1.0.0.0.1434)
- [ ] 12.1.0-hf1 (BIGIP-12.1.0.1.0.1447-HF1)
- [ ] 12.1.0-hf2 (BIGIP-12.1.0.2.0.1468-HF2)
- [ ] 12.1.1 (BIGIP-12.1.1.0.0.184)
- [ ] 12.1.1-hf1 (BIGIP-12.1.1.1.0.196-HF1)
- [ ] 12.1.1-hf2 (BIGIP-12.1.1.2.0.204-HF2)
- [ ] 12.1.2 (BIGIP-12.1.2.0.0.249)
- [ ] 12.1.2-hf1 (BIGIP-12.1.2.1.0.264-HF1)
- [ ] 13.0.0 (BIGIP-13.0.0.0.0.1645)

##### CHECKLIST
<!---
Ensure all the following are complete
-->
#### Module code related
- [ ] Module code has `EXAMPLES`
- [ ] Module code has `DOCUMENTATION`
- [ ] Module code has `RETURN`
- [ ] Module code has `ANSIBLE_METADATA`
- [ ] Module code conforms to coding standards (v3). This includes a `Parameters` class, `ModuleManager` class, and `ArgumentSpec` class.
- [ ] Module includes GPL3 license at top of the file and F5 Networks copyright.
- [ ] Module imports are not `from *`

#### Integration test related
- [ ] Playbook exists to do functional tests
- [ ] Role directory with functional tests exists
- [ ] Module code has been tested on major releases post 12.x. If a major release cannot be supported, document "why" in the `notes` section of the module 
`DOCUMENTATION`

#### Unit test related
- [ ] Unit tests in `tests/unit` for the product exist
- [ ] `TestParameters` unit test class exists and has content
- [ ] `TestManager` unit test class exists and has contents

#### QC related
- [ ] Module code passes `tox -e flake -- library/MODULE_NAME.py`
- [ ] Unit test code passes `tox -e flake -- test/unit/PRODUCT/test_MODULE_NAME.py`

#### Docs related
- [ ] Docs exist and build correctly (`make docs`)
- [ ] Docs have been merged to `f5-ansible` so they can be rebuilt by ReadTheDocs.

#### Upstream vendor related
- [ ] Module code in Ansible repo passes `ansible-test units --tox --python 2.6 MODULE_NAME.py`
- [ ] Module code in Ansible repo passes `ansible-test units --tox --python 2.7 MODULE_NAME.py`
- [ ] Module code in Ansible repo passes `ansible-test units --tox --python 3.5 MODULE_NAME.py`
- [ ] Module code in Ansible repo passes `ansible-test units --tox --python 3.6 MODULE_NAME.py`


##### SUMMARY
<!--- Explain the problem briefly -->
