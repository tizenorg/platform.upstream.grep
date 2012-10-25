Name:           grep
BuildRequires:  automake
BuildRequires:  pcre-devel
Url:            http://www.gnu.org/software/grep/
Provides:       base:/usr/bin/grep
Version:        2.14
Release:        0
Summary:        Print lines matching a pattern
License:        GPL-3.0+
Group:          Productivity/Text/Utilities
Source0:        grep-%{version}.tar.xz

%description
The grep command searches one or more input files for lines
containing a match to a specified pattern.  By default, grep prints
the matching lines.

%prep
%setup -q

%build
%configure --disable-silent-rules --without-included-regex
%{__make} %{?_smp_mflags}

%check
make check VERBOSE=1

%install
%make_install
%find_lang %name


%docs_package

%lang_package

%files 
%defattr(-,root,root)
%{_bindir}/*

%changelog
