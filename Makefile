PROJECT=mangezmieux
PKGDIR=debian/$(PROJECT)
CODEDIR=$(PKGDIR)/usr/share
GITFILES=".git*"

install:
	mkdir -p $(CODEDIR)
	cp -r $(PROJECT) $(CODEDIR)/
clean:
	find debian/ -maxdepth 1 ! -name "*control" -a ! -name "*rules" -a ! -name "debian" -a ! -name "*changelog" -a ! -name "*compat" -a ! -name "*copyright" -a ! -name "*postinst" -exec rm -rf {} \;
