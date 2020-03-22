Summary:	Personal job scheduler
Name:		task-spooler
Version:	1.0
Release:	0.1
License:	GPL v2+
Group:		Applications
URL:		http://vicerveza.homeunix.net/~viric/soft/ts
Source0:	%{url}/ts-%{version}.tar.gz
# Source0-md5:	c7589cdc28115d8925794d713ff72dba
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Task spooler is a Unix batch system where the tasks spooled run one
after the other. Each user in each system has his own job queue. The
tasks are run in the correct context (that of enqueue) from any
shell/process, and its output/results can be easily watched. It is
very useful when you know that your commands depend on a lot of RAM, a
lot of disk use, give a lot of output, or for whatever reason it's
better not to run them at the same time.

%prep
%setup -qn ts-%{version}

%build
%{__make} \
	LDFLAGS="%{rpmldflags}" \
	CFLAGS="%{rpmcflags} -pedantic -ansi" \
	CPPFLAGS="%{rpmcppflags} -D_XOPEN_SOURCE=500 -D__STRICT_ANSI__" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

mv $RPM_BUILD_ROOT%{_bindir}/ts $RPM_BUILD_ROOT%{_bindir}/tsp
mv $RPM_BUILD_ROOT%{_mandir}/man1/ts.1 $RPM_BUILD_ROOT%{_mandir}/man1/tsp.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README TRICKS PROTOCOL
%attr(755,root,root) %{_bindir}/tsp
%{_mandir}/man1/tsp.1.*
