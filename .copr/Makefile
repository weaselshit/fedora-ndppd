srpm:
	dnf -y install wget rpkg
	wget https://github.com/DanielAdolfsson/ndppd/archive/master.tar.gz
	rpkg srpm
	mv *.src.rpm "$(outdir)"
