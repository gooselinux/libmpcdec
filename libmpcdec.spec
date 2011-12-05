
Summary: Musepack audio decoding library
Name:	 libmpcdec
Version: 1.2.6
Release: 6.1%{?dist}

License: BSD 
Group: 	 System Environment/Libraries
URL: 	 http://www.musepack.net/
Source0: http://files.musepack.net/source/libmpcdec-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Musepack is an audio compression format with a strong emphasis on high quality.
It's not lossless, but it is designed for transparency, so that you won't be
able to hear differences between the original wave file and the much smaller
MPC file.
It is based on the MPEG-1 Layer-2 / MP2 algorithms, but has rapidly developed
and vastly improved and is now at an advanced stage in which it contains
heavily optimized and patentless code.

%package devel
Summary: Development files for the Musepack audio decoding library
Group:	 Development/Libraries
Requires: %{name} = %{version}-%{release}
%description devel
%{summary}.


%prep
%setup -q


%build
%configure --disable-static

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

#Unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.la


%clean
rm -rf $RPM_BUILD_ROOT 


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/lib*.so


%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.2.6-6.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 08 2008 Rex Dieter <rdieter@fedoraproject.org> 1.2.6-4
- respin (gcc43)

* Sat Aug 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.2.6-3
- respin (BuildID)

* Wed Jun 06 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.2.6-2
- fix %%files (docs/html is no more)

* Wed Jun 06 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.2.6-1
- libmpcdec-1.2.6

* Tue Aug 29 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.2.2-4
- fc6 respin

* Wed Aug 09 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.2.2-3
- fc6 respin

* Sat Apr 01 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.2.2-2
- License: BSD

* Thu Jan 19 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.2.2-1
- libmpcdec-1.2.2

* Thu Jan 19 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.1-2
- cleanup

* Fri Jun 17 2005 Mihai Maties <mihai@xcyb.org> 1.1-1
- update to 1.1
- changed license to BSD
- updated the spec to use autotools

* Fri Nov 26 2004 Matthias Saou <http://freshrpms.net/> 1.0.2-1
- Initial RPM release.
- Include the mandatory copy of the LGPL (there is none in the sources...).

