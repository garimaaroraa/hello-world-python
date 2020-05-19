# hello-world-python
Test python package with github 

### Releasing

- `make bump_patch_version`
- Update [the Changelog]
- Commit changes to `Changelog`, `setup.py` and `setup.cfg`.
- `make release` (this'll push a tag that will trigger a Drone build)
