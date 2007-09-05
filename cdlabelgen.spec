%include	/usr/lib/rpm/macros.perl
Summary:	cdlabelgen - generates frontcards and traycards for CDs
Summary(pl.UTF-8):	Program do generowania wkładek do pudełek na płyty CD
Name:		cdlabelgen
Version:	4.0.0
Release:	1
License:	GPL
Vendor:		B. W. Fitzpatrick <fitz@red-bean.com>
Group:		Applications/Text
Source0:	http://www.aczoom.com/pub/tools/%{name}-%{version}.tgz
# Source0-md5:	0b8225fd914b5c7aa1d3e616b1c8accc
URL:		http://www.aczoom.com/tools/cdinsert/
BuildRequires:	perl-devel >= 1:5.6.1
BuildRequires:	perl-tools-pod
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
This is BETA software! Please be gentle. cdlabelgen was designed to
simplify the process of generating labels for CD's. It originated as a
program to allow auto generation of frontcards and traycards for CD's
burned via an automated mechanism (specifically for archiving data).
Note that cdlabelgen does not actually print anything--it just spits
out postscript, which you can then do with as you please.

%description -l pl.UTF-8
Program ten jest w fazie beta! Prosimy o wyrozumiałość. Cdlabelgen
napisano w celu uproszczenia procesu tworzenia etykiet na CD. Powstał
jako projekt, który miał pomóc w automatycznej generacji wkładek do
pudełek na wypalane płyty CD (zwłaszcza przy archiwizacji danych).
Należy zwrócić uwagę, że cdlabelgen sam w sobie nic nie drukuje,
tworzy jedynie plik postscriptowy, który można samemu wydrukować.

%prep
%setup -q

%build
pod2man --section=1 cdlabelgen.pod > cdlabelgen.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}}

%{__make} install \
	BASE_DIR=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/cdlabelgen
%{_mandir}/man1/cdlabelgen.1*
%{_datadir}/cdlabelgen
