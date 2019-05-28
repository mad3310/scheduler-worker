%if 0%{?rhel} && 0%{?rhel} <= 6
	%{!?__python2: %global __python2 /usr/bin/python2}
	%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
	%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%else
	%global __python2 /usr/bin/python
%endif

%define name scheduler-worker
%define version 1.0.0
%define unmangled_version 1.0.0
%define release 1

Name: %{name}
Version:	%{version}
Release:	%{release}
Summary:scheduler-worker	

Group:	SupplyChain
License: MPLv2.0
URL:http://code.ds.gome.com.cn/gitlab/gscm/gscm-git/scheduler-worker		
Source0: %{name}-%{unmangled_version}.tar.gz
Source1: %{name}.conf
Source2: %{name}.service
Vendor: SupplyChain
Buildarch: noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot	

BuildRequires:	systemd-units
Requires: systemd python-requests 	

%description

%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
%post
%systemd_post %{name}.service
 
%preun
%systemd_preun %{name}.service
 
%postun
%systemd_postun_with_restart %{name}.service
%else
%post
/sbin/chkconfig --add %{name}
 
%preun
if [ "$1" = 0 ] ; then
    /sbin/service %{name} stop >/dev/null 2>&1
    /sbin/chkconfig --del %{name}
fi
%endif

%prep
%setup -n %{name}-%{unmangled_version}

%clean
rm -rf %{buildroot}


%build
python setup.py build


%install
python setup.py install --skip-build --root=%{buildroot}
#mkdir -p %{buildroot}/%{_bindir}
#cp %{SOURCE0} %{buildroot}/%{_bindir}
#mkdir -p %{buildroot}/%{_sysconfdir}/%{name}/
#cp %{SOURCE1} %{buildroot}/%{_sysconfdir}/%{name}/
mkdir -p %{buildroot}/%{_unitdir}
cp %{SOURCE2} %{buildroot}/%{_unitdir}/
mkdir -p %{buildroot}/var/log/%{name}


%files
%{python_sitelib}/scheduler_worker
%defattr(-,root,root,-)
#%config(noreplace) %attr(-,root,root) %{_sysconfdir}/%{name}/%{name}.conf
%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
	%{_unitdir}/%{name}.service
%else
	%{_initrddir}/%{name}
	%{_sysconfdir}/logrotate.d/%{name}
%endif
#%attr(755, root, root) %{_bindir}/%{name}
/var/log/%{name}



%changelog
