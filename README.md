# Salt Extension for Elasticsearch

Salt Extension for interacting with Elasticsearch

## Security

If you think you've found a security vulnerability, see
[Salt's security guide][security].

## User Documentation

This README is for people aiming to contribute to the project.
If you just want to get started with the extension, check out the
module docstrings (for now, documentation is coming!).

## Contributing

The saltext-elasticsearch project team welcomes contributions from the community.

The [Salt Contributing guide][salt-contributing] has a lot of relevant
information, but if you'd like to jump right in here's how to get started:


```bash
# Clone the repo
git clone --origin salt git@github.com:salt-extensions/saltext-elasticsearch.git

# Change to the repo dir
cd saltext-elasticsearch

# Create a new venv
python3 -m venv env --prompt saltext-elasticsearch
source env/bin/activate

# On mac, you may need to upgrade pip
python -m pip install --upgrade pip

# On WSL or some flavors of linux you may need to install the `enchant`
# library in order to build the docs
sudo apt-get install -y enchant

# Install extension + test/dev/doc dependencies into your environment
python -m pip install -e '.[tests,dev,docs]'

# Run tests!
python -m nox -e tests-3

# skip requirements install for next time
export SKIP_REQUIREMENTS_INSTALL=1

# Build the docs, serve, and view in your web browser:
python -m nox -e docs && (cd docs/_build/html; python -m webbrowser localhost:8000; python -m http.server; cd -)
```

Writing code isn't the only way to contribute! We value contributions in any of
these areas:

* Documentation - especially examples of how to use this module to solve
  specific problems.
* Triaging [issues][issues] and participating in [discussions][discussions]
* Reviewing [Pull Requests][PRs] (we really like
  [Conventional Comments][comments]!)

You could also contribute in other ways:

* Writing blog posts
* Posting on social media about how you used Salt+Elasticsearch to solve your
  problems, including videos
* Giving talks at conferences
* Publishing videos
* Asking/answering questions in IRC, Slack, or email groups

Any of these things are super valuable to our community, and we sincerely
appreciate every contribution!


For more information, build the docs and head over to http://localhost:8000/ —
that's where you'll find the rest of the documentation.


[security]: https://github.com/saltstack/salt/blob/master/SECURITY.md
[salt-contributing]: https://docs.saltproject.io/en/master/topics/development/contributing.html
[issues]: https://github.com/salt-extensions/saltext-elasticsearch/issues
[PRs]: https://github.com/salt-extensions/saltext-elasticsearch/pulls
[discussions]: https://github.com/salt-extensions/saltext-elasticsearch/discussions
[comments]: https://conventionalcomments.org/
