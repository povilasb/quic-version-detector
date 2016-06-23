python := python3
src_dir := quic_version_detector

virtualenv_dir := pyenv
pip := $(virtualenv_dir)/bin/pip
pytest := $(virtualenv_dir)/bin/py.test
coverage := $(virtualenv_dir)/bin/coverage


test: $(virtualenv_dir)
	PYTHONPATH=$(PYTHONPATH):. $(coverage) run \
		--source $(src_dir) $(pytest) -s tests
	$(coverage) report -m
.PHONY: test

$(virtualenv_dir): requirements/dev.txt
	virtualenv $@ --python=$(python)
	$(pip) install -r $^
