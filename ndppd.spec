%{!?commit: %global commit %(git rev-parse HEAD)}
%{!?gitdate: %global gitdate %(git rev-list --max-count=1 --date=format:%Y%m%d --pretty=format:%cd %{commit} | tail -1)}
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: ndppd
Version: 0.2.5.999
Release: 2.%{gitdate}git%{shortcommit}%{?dist}
Summary: NDP Proxy Daemon

Group: System Environment/Daemons
License: GPL-3
URL: https://github.com/DanielAdolfsson/ndppd
Source0: https://github.com/DanielAdolfsson/%{name}/archive/master.tar.gz
Source1: ndppd.service

BuildRequires: gcc
BuildRequires: make
BuildRequires: systemd-units

%description
'ndppd', or NDP Proxy Daemon, is a daemon that proxies NDP (Neighbor 
Discovery Protocol) messages between interfaces.

%prep
%setup -n %{name}-master

%build
make %{?_smp_mflags} CXXFLAGS="%{optflags}"

%install
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/run/ndppd
%make_install PREFIX=/usr
install -Dt ${RPM_BUILD_ROOT}%{_unitdir} -m 644 %{SOURCE1}


%postun
%systemd_postun_with_restart ndppd.service

%post
%systemd_post ndppd.service

%preun
%systemd_preun ndppd.service

%files
%doc ChangeLog LICENSE README
%{_unitdir}/ndppd.service
/usr/sbin/ndppd
/usr/share/man/man1/ndppd.1.gz
/usr/share/man/man5/ndppd.conf.5.gz
%dir %{_localstatedir}/run/ndppd/

%changelog
* Tue May 16 2017 Dick Marinus <dick@mrns.nl> - 0.2.5-1
- initial package                                                                                          

