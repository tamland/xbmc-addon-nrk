ADDON_NAME := $(shell grep '<addon id="' addon.xml |cut -d\" -f2)
VERSION := $(shell grep '  version=' addon.xml |cut -d\" -f2)
FILES = addon.py addon.xml changelog.txt fanart.jpg icon.png LICENSE.txt \
  main.py nrktv.py resources subs.py
REPO_PLUGINS ?= ../repo-plugins
RELEASE_BRANCH ?= nexus

all: dist

dist:
	mkdir -p tmpdir/$(ADDON_NAME)
	cp -r $(FILES) tmpdir/$(ADDON_NAME)/
	(cd tmpdir; zip -r ../$(ADDON_NAME)-$(VERSION).zip $(ADDON_NAME)/ \
		--exclude \*.pyc)
	rm -r tmpdir/$(ADDON_NAME)
	rmdir tmpdir

prepare_release:
	[ -d "$(REPO_PLUGINS)" ] || \
		git clone --depth 5 -b $(RELEASE_BRANCH) https://github.com/xbmc/repo-scripts "$(REPO_PLUGINS)"
	git -C $(REPO_PLUGINS) stash
	git -C $(REPO_PLUGINS) checkout $(RELEASE_BRANCH)
	rm -rf $(REPO_PLUGINS)/$(ADDON_NAME)
	mkdir $(REPO_PLUGINS)/$(ADDON_NAME)
	cp -r $(FILES) $(REPO_PLUGINS)/$(ADDON_NAME)/

clean:
	rm *.zip
