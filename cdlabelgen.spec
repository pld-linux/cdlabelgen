%include	/usr/lib/rpm/macros.perl
Summary:	cdlabelgen - generates frontcards and traycards for CDs
Summary(pl):	Program do generowania wk³adek do pude³ek na p³yty CD
Name:		cdlabelgen
Version:	2.6.1
Release:	2
License:	GPL
Vendor:		B. W. Fitzpatrick <fitz@red-bean.com>
Group:		Applications/Text
Source0:	http://www.aczone.com/pub/tools/%{name}-%{version}.tgz
# Source0-md5:	3bca1861177c1624a45806f814a4839d
Patch0:		%{name}-manlocation.patch
URL:		http://www.aczone.com/tools/cdinsert/
BuildRequires:	perl-devel >= 1:5.6.1
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

%description -l pl
Program ten jest w fazie beta! Prosimy o wyrozumia³o¶æ. Cdlabelgen
napisano w celu uproszczenia procesu tworzenia etykiet na CD. Powsta³
jako projekt, który mia³ pomóc w automatycznej generacji wk³adek do
pude³ek na wypalane p³yty CD (zw³aszcza przy archiwizacji danych).
Nale¿y zwróciæ uwagê, ¿e cdlabelgen sam w sobie nic nie drukuje,
tworzy jedynie plik postscriptowy, który mo¿na samemu wydrukowaæ.

%prep
%setup -q
%patch0 -p0

%build
pod2man --section=1 cdlabelgen > cdlabelgen.1

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
