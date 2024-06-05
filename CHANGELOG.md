# 1.0.0 (Wed Jun 05 2024)

#### 💥 Breaking Change

- Rebrand into fscacher-pkgtester (python package remains the same) [#1](https://github.com/neurodebian/fscacher-pkgtester/pull/1) ([@yarikoptic](https://github.com/yarikoptic))

#### ⚠️ Pushed to `master`

- Add a few folders I found locally into git ignore ([@yarikoptic](https://github.com/yarikoptic))
- Unify asv requirements ([@jwodder](https://github.com/jwodder))
- Do not do manual installation of asv, use our setup.cfg etc ([@yarikoptic](https://github.com/yarikoptic))
- Restrict asv to come before 0.6.2 since causes CI fail ([@yarikoptic](https://github.com/yarikoptic))
- Remove remainder of 3.7 mentionings ([@yarikoptic](https://github.com/yarikoptic))
- Stop using/testing EOLed 3.6 and 3.7, use 3.9 for linting (3.8 EOLs soon) ([@yarikoptic](https://github.com/yarikoptic))
- Set CODECOV_TOKEN ([@jwodder](https://github.com/jwodder))
- [gh-actions](deps): Bump codecov/codecov-action from 3 to 4 ([@dependabot[bot]](https://github.com/dependabot[bot]))
- [gh-actions](deps): Bump actions/setup-python from 4 to 5 ([@dependabot[bot]](https://github.com/dependabot[bot]))
- Test against Python 3.12 and PyPy 3.10 ([@jwodder](https://github.com/jwodder))
- Replace appdirs with platformdirs ([@jwodder](https://github.com/jwodder))
- Use Python 3.8 to test against dev version of joblib ([@jwodder](https://github.com/jwodder))
- [gh-actions](deps): Bump actions/checkout from 3 to 4 ([@dependabot[bot]](https://github.com/dependabot[bot]))
- Add packaging to dependencies along with asv as instructed in the issue ([@yarikoptic](https://github.com/yarikoptic))
- ASV dropped --strict option in 0.6.0 release ([@yarikoptic](https://github.com/yarikoptic))
- Update README ([@jwodder](https://github.com/jwodder))
- Add `exclude_kwargs` to memoization decorators ([@yarikoptic](https://github.com/yarikoptic))
- Further testing ([@jwodder](https://github.com/jwodder))
- Update README.rst ([@jwodder](https://github.com/jwodder))
- Update src/fscacher/cache.py ([@jwodder](https://github.com/jwodder))
- Ignore cache for non-path-like arguments ([@jwodder](https://github.com/jwodder))
- Boilerplate updates ([@jwodder](https://github.com/jwodder))
- Skip a test on PyPy on Windows ([@jwodder](https://github.com/jwodder))
- Test against more recent versions of PyPy ([@jwodder](https://github.com/jwodder))
- Merge branch 'master' into no-py3.6 ([@yarikoptic](https://github.com/yarikoptic))
- Drop support for Python 3.6 ([@jwodder](https://github.com/jwodder))
- Test against Python 3.11 ([@jwodder](https://github.com/jwodder))
- Configure Dependabot to update GitHub Actions action versions ([@jwodder](https://github.com/jwodder))
- Update GitHub Actions action versions ([@jwodder](https://github.com/jwodder))
- Clean out vfat mount between benchmarks ([@jwodder](https://github.com/jwodder))
- Test that file order is irrelevant for DirFingerprints ([@jwodder](https://github.com/jwodder))
- Try to make bytes-XORing faster ([@jwodder](https://github.com/jwodder))
- Make benchmarks measure cache misses and hits separately ([@jwodder](https://github.com/jwodder))
- Fix ([@jwodder](https://github.com/jwodder))
- Improve benchmark workflow's handling of errors ([@jwodder](https://github.com/jwodder))
- Support specifying a custom path for the cache ([@jwodder](https://github.com/jwodder))
- Cache directory fingerprint as a XORed hash of file fingerprints ([@jwodder](https://github.com/jwodder))
- Don't fingerprint paths when caching is ignored ([@jwodder](https://github.com/jwodder))
- Update Python version used to test development joblib to 3.7 ([@jwodder](https://github.com/jwodder))
- Run isort and flake8 with pre-commit ([@jwodder](https://github.com/jwodder))
- Stop using flake8-import-order-jwodder; starting using flake8-unused-arguments ([@jwodder](https://github.com/jwodder))
- Give linters their own tox env ([@jwodder](https://github.com/jwodder))
- Handle functions whose first arguments aren't named "path" ([@jwodder](https://github.com/jwodder))
- make joblib ignore "path" , pass resolved as part of the fingerprinting kwargs arg ([@yarikoptic](https://github.com/yarikoptic))
- Capture all logs during tests ([@jwodder](https://github.com/jwodder))
- Make versioneer.py use setuptools instead of distutils ([@jwodder](https://github.com/jwodder))
- Update codecov action to v2 ([@jwodder](https://github.com/jwodder))
- Ignore DeprecationWarning caused by joblib using distutils ([@jwodder](https://github.com/jwodder))
- Test against Python 3.10 ([@jwodder](https://github.com/jwodder))
- Revert "Limit joblib version to pre-1.1.0" ([@jwodder](https://github.com/jwodder))
- Fix how asv is told to use the current Python version ([@jwodder](https://github.com/jwodder))
- Change pypy3 to pypy-3.7 on GitHub Actions ([@jwodder](https://github.com/jwodder))
- Limit joblib version to pre-1.1.0 ([@jwodder](https://github.com/jwodder))
- Install git annex in non-Windows CI environments ([@jwodder](https://github.com/jwodder))
- Test handling of moving symlinks around in git-annex ([@jwodder](https://github.com/jwodder))
- Update for dev version of joblib ([@jwodder](https://github.com/jwodder))
- Test against dev version of joblib ([@jwodder](https://github.com/jwodder))
- Resimplify release workflow ([@jwodder](https://github.com/jwodder))
- Remove debug step ([@jwodder](https://github.com/jwodder))
- Fix versioneer+auto integration (or else) ([@jwodder](https://github.com/jwodder))
- Try to debug versioneer failure ([@jwodder](https://github.com/jwodder))
- Get auto and versioneer to play nice together ([@jwodder](https://github.com/jwodder))
- Get asv to run pypy3 correctly ([@jwodder](https://github.com/jwodder))
- Remove newlines from test files, as they differ on Windows ([@jwodder](https://github.com/jwodder))
- Test against Windows and macOS ([@jwodder](https://github.com/jwodder))
- Set up auto ([@jwodder](https://github.com/jwodder))
- Start CHANGELOG ([@jwodder](https://github.com/jwodder))
- v0.1.0 — Initial release ([@jwodder](https://github.com/jwodder))
- Keywords & classifiers ([@jwodder](https://github.com/jwodder))
- Add structure to README ([@jwodder](https://github.com/jwodder))
- Include inode in file fingerprints ([@jwodder](https://github.com/jwodder))
- Fill in README ([@jwodder](https://github.com/jwodder))
- RF(BM): do not bother with custom options -- do not help, and also do loop explicitly as we had it ([@yarikoptic](https://github.com/yarikoptic))
- ENH: establish Benchmark base class with common parameters to stabilize benchmarking ([@yarikoptic](https://github.com/yarikoptic))
- RF(BM): make time_{file,directory} to have only invoking already for a cached result ([@yarikoptic](https://github.com/yarikoptic))
- ENH: install also pre-commit for devel ([@yarikoptic](https://github.com/yarikoptic))
- RF(BM): remove "n" parameter, should not be needed ([@yarikoptic](https://github.com/yarikoptic))
- ENH: set benchmarks (and devel and all) extra_require ([@yarikoptic](https://github.com/yarikoptic))
- Make benchmark workflow fail if a benchmark slowed down too much ([@jwodder](https://github.com/jwodder))
- RM: do not run bechmarking on push ([@yarikoptic](https://github.com/yarikoptic))
- Make asv only benchmark the latest commit at a time ([@jwodder](https://github.com/jwodder))
- Lint ([@jwodder](https://github.com/jwodder))
- Run benchmarks on multiple file systems ([@jwodder](https://github.com/jwodder))
- Fetch history when benchmarking ([@jwodder](https://github.com/jwodder))
- Benchmarking workflow ([@jwodder](https://github.com/jwodder))
- Basic benchmarking with asv ([@jwodder](https://github.com/jwodder))
- Support fingerprinting directories ([@jwodder](https://github.com/jwodder))
- Replace DANDI_CACHE with FSCACHER_CACHE and custom envvar ([@jwodder](https://github.com/jwodder))
- Use "fscacher" for appdir name instead of "dandi" ([@jwodder](https://github.com/jwodder))
- Update repo URLs ([@jwodder](https://github.com/jwodder))
- Update .gitattributes ([@jwodder](https://github.com/jwodder))
- Added GitHub Actions workflow ([@jwodder](https://github.com/jwodder))
- Simplify flake8 config for black compatibility ([@jwodder](https://github.com/jwodder))
- Rename to fscacher ([@jwodder](https://github.com/jwodder))
- Move tests under package ([@jwodder](https://github.com/jwodder))
- Use pre-commit ([@jwodder](https://github.com/jwodder))
- Support `from pyfscacher import PersistentCache` ([@jwodder](https://github.com/jwodder))
- Successfully test ([@jwodder](https://github.com/jwodder))
- Copy tests from https://github.com/dandi/dandi-cli/blob/master/dandi/support/tests/test_cache.py ([@jwodder](https://github.com/jwodder))
- Use versioneer ([@jwodder](https://github.com/jwodder))
- Packaging ([@jwodder](https://github.com/jwodder))
- Remove dependence on get_logger() ([@jwodder](https://github.com/jwodder))
- Copy code from https://github.com/dandi/dandi-cli/blob/master/dandi/support/cache.py ([@jwodder](https://github.com/jwodder))
- Initial commit ([@yarikoptic](https://github.com/yarikoptic))

#### Authors: 3

- [@dependabot[bot]](https://github.com/dependabot[bot])
- John T. Wodder II ([@jwodder](https://github.com/jwodder))
- Yaroslav Halchenko ([@yarikoptic](https://github.com/yarikoptic))

---

# 0.4.1 (Tue Jun 04 2024)

#### 🐛 Bug Fix

- Stop using/testing EOLed 3.6 and 3.7, use 3.9 for linting (3.8 EOLs soon) [#91](https://github.com/con/fscacher/pull/91) ([@yarikoptic](https://github.com/yarikoptic) [@jwodder](https://github.com/jwodder))
- ASV dropped --strict option  in 0.6.0 release [#83](https://github.com/con/fscacher/pull/83) ([@yarikoptic](https://github.com/yarikoptic))

#### 🏠 Internal

- Add a few folders I found locally into git ignore [#92](https://github.com/con/fscacher/pull/92) ([@yarikoptic](https://github.com/yarikoptic))
- [gh-actions](deps): Bump codecov/codecov-action from 3 to 4 [#89](https://github.com/con/fscacher/pull/89) ([@dependabot[bot]](https://github.com/dependabot[bot]) [@jwodder](https://github.com/jwodder))
- [gh-actions](deps): Bump actions/setup-python from 4 to 5 [#88](https://github.com/con/fscacher/pull/88) ([@dependabot[bot]](https://github.com/dependabot[bot]))
- [gh-actions](deps): Bump actions/checkout from 3 to 4 [#82](https://github.com/con/fscacher/pull/82) ([@dependabot[bot]](https://github.com/dependabot[bot]))

#### 🧪 Tests

- Test against Python 3.12 and PyPy 3.10 [#84](https://github.com/con/fscacher/pull/84) ([@jwodder](https://github.com/jwodder))
- Use Python 3.8 to test against dev version of joblib [#86](https://github.com/con/fscacher/pull/86) ([@jwodder](https://github.com/jwodder))

#### 🔩 Dependency Updates

- Replace appdirs with platformdirs [#85](https://github.com/con/fscacher/pull/85) ([@jwodder](https://github.com/jwodder))

#### Authors: 3

- [@dependabot[bot]](https://github.com/dependabot[bot])
- John T. Wodder II ([@jwodder](https://github.com/jwodder))
- Yaroslav Halchenko ([@yarikoptic](https://github.com/yarikoptic))

---

# 0.4.0 (Wed Aug 16 2023)

#### 🚀 Enhancement

- Add `exclude_kwargs` to memoization decorators [#38](https://github.com/con/fscacher/pull/38) ([@yarikoptic](https://github.com/yarikoptic) [@jwodder](https://github.com/jwodder))

#### Authors: 2

- John T. Wodder II ([@jwodder](https://github.com/jwodder))
- Yaroslav Halchenko ([@yarikoptic](https://github.com/yarikoptic))

---

# 0.3.0 (Mon Feb 20 2023)

#### 🚀 Enhancement

- Ignore cache for non-path-like arguments [#79](https://github.com/con/fscacher/pull/79) ([@jwodder](https://github.com/jwodder))

#### 🐛 Bug Fix

- Drop support for Python 3.6 [#80](https://github.com/con/fscacher/pull/80) ([@jwodder](https://github.com/jwodder) [@yarikoptic](https://github.com/yarikoptic))

#### 🏠 Internal

- Update GitHub Actions action versions [#77](https://github.com/con/fscacher/pull/77) ([@jwodder](https://github.com/jwodder))

#### 🧪 Tests

- Test against more recent versions of PyPy [#81](https://github.com/con/fscacher/pull/81) ([@jwodder](https://github.com/jwodder))
- Test against Python 3.11 [#78](https://github.com/con/fscacher/pull/78) ([@jwodder](https://github.com/jwodder))
- Clean out vfat mount between benchmarks [#76](https://github.com/con/fscacher/pull/76) ([@jwodder](https://github.com/jwodder))

#### Authors: 2

- John T. Wodder II ([@jwodder](https://github.com/jwodder))
- Yaroslav Halchenko ([@yarikoptic](https://github.com/yarikoptic))

---

# 0.2.0 (Tue Feb 22 2022)

#### 🚀 Enhancement

- Support specifying a custom path for the cache; tokens becomes kwonly [#73](https://github.com/con/fscacher/pull/73) ([@jwodder](https://github.com/jwodder))
- make joblib ignore "path" , pass resolved as part of the fingerprinting kwargs arg [#63](https://github.com/con/fscacher/pull/63) ([@yarikoptic](https://github.com/yarikoptic) [@jwodder](https://github.com/jwodder))

#### 🏎 Performance

- Cache directory fingerprint as a XORed hash of file fingerprints [#71](https://github.com/con/fscacher/pull/71) ([@jwodder](https://github.com/jwodder))
- Don't fingerprint paths when caching is ignored [#72](https://github.com/con/fscacher/pull/72) ([@jwodder](https://github.com/jwodder))

#### 🏠 Internal

- Improve linting configuration [#64](https://github.com/con/fscacher/pull/64) ([@jwodder](https://github.com/jwodder))
- Make versioneer.py use setuptools instead of distutils [#54](https://github.com/con/fscacher/pull/54) ([@jwodder](https://github.com/jwodder))
- Update codecov action to v2 [#53](https://github.com/con/fscacher/pull/53) ([@jwodder](https://github.com/jwodder))

#### 🧪 Tests

- Make benchmarks measure cache misses and hits separately [#74](https://github.com/con/fscacher/pull/74) ([@jwodder](https://github.com/jwodder))
- Update Python version used to test development joblib to 3.7 [#65](https://github.com/con/fscacher/pull/65) ([@jwodder](https://github.com/jwodder))
- Capture all logs during tests [#56](https://github.com/con/fscacher/pull/56) ([@jwodder](https://github.com/jwodder))

#### Authors: 2

- John T. Wodder II ([@jwodder](https://github.com/jwodder))
- Yaroslav Halchenko ([@yarikoptic](https://github.com/yarikoptic))

---

# 0.1.6 (Thu Oct 07 2021)

#### 🐛 Bug Fix

- Revert "Limit joblib version to pre-1.1.0" [#52](https://github.com/con/fscacher/pull/52) ([@jwodder](https://github.com/jwodder))

#### 🧪 Tests

- Test against Python 3.10 [#49](https://github.com/con/fscacher/pull/49) ([@jwodder](https://github.com/jwodder))
- Change pypy3 to pypy-3.7 on GitHub Actions [#50](https://github.com/con/fscacher/pull/50) ([@jwodder](https://github.com/jwodder))

#### Authors: 1

- John T. Wodder II ([@jwodder](https://github.com/jwodder))

---

# 0.1.5 (Thu Oct 07 2021)

#### 🐛 Bug Fix

- Limit joblib version to pre-1.1.0 [#48](https://github.com/con/fscacher/pull/48) ([@jwodder](https://github.com/jwodder))
- Test against and update for dev version of joblib [#42](https://github.com/con/fscacher/pull/42) ([@jwodder](https://github.com/jwodder))

#### 🏠 Internal

- Resimplify release workflow [#35](https://github.com/con/fscacher/pull/35) ([@jwodder](https://github.com/jwodder))
- Remove debug step [#34](https://github.com/con/fscacher/pull/34) ([@jwodder](https://github.com/jwodder))

#### 🧪 Tests

- Test handling of moving symlinks around in git-annex [#47](https://github.com/con/fscacher/pull/47) ([@jwodder](https://github.com/jwodder))

#### Authors: 1

- John T. Wodder II ([@jwodder](https://github.com/jwodder))

---

# 0.1.4 (Mon Feb 22 2021)

#### 🐛 Bug Fix

- Fix versioneer+auto integration (or else) [#33](https://github.com/con/fscacher/pull/33) ([@jwodder](https://github.com/jwodder))

#### Authors: 1

- John T. Wodder II ([@jwodder](https://github.com/jwodder))

---

# 0.1.3 (Mon Feb 22 2021)

#### 🐛 Bug Fix

- Try to debug versioneer failure [#32](https://github.com/con/fscacher/pull/32) ([@jwodder](https://github.com/jwodder))

#### Authors: 1

- John T. Wodder II ([@jwodder](https://github.com/jwodder))

---

# 0.1.2 (Mon Feb 22 2021)

#### 🐛 Bug Fix

- Get auto and versioneer to play nice together [#31](https://github.com/con/fscacher/pull/31) ([@jwodder](https://github.com/jwodder))

#### Authors: 1

- John T. Wodder II ([@jwodder](https://github.com/jwodder))

---

# 0.1.1 (Mon Feb 22 2021)

#### 🐛 Bug Fix

- Get tests to pass on Windows and macOS [#29](https://github.com/con/fscacher/pull/29) ([@jwodder](https://github.com/jwodder))

#### ⚠️ Pushed to `master`

- Start CHANGELOG ([@jwodder](https://github.com/jwodder))

#### 🏠 Internal

- Set up auto [#27](https://github.com/con/fscacher/pull/27) ([@jwodder](https://github.com/jwodder))

#### 🧪 Tests

- Get asv to run pypy3 correctly [#30](https://github.com/con/fscacher/pull/30) ([@jwodder](https://github.com/jwodder))

#### Authors: 1

- John T. Wodder II ([@jwodder](https://github.com/jwodder))

---

# v0.1.0 (2021-02-18)

Initial release
