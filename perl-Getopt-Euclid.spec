#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Getopt
%define	pnam	Euclid
Summary:	Getopt::Euclid - Executable Uniform Command-Line Interface Descriptions
Summary(pl.UTF-8):	Getopt::Euclid - ujednolicone opisy interfejsu linii poleceń
Name:		perl-Getopt-Euclid
Version:	0.3.2
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Getopt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	70de1b3351f52ba8a741c1e7d51049b0
URL:		http://search.cpan.org/dist/Getopt-Euclid/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-version
BuildRequires:	perltidy
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Getopt::Euclid uses your program's own documentation to create a
command-line argument parser. This ensures that your program's
documented interface and its actual interface always agree.

%description -l pl.UTF-8
Getopt::Euclid wykorzystuje dokumentację programu do utworzenia
analizatora argumentów linii poleceń. Daje to pewność, że
udokumentowany i faktyczny interfejs programu będą się zawsze zgadzać.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Getopt/*.pm
%{perl_vendorlib}/Getopt/Euclid
%{_mandir}/man3/*
