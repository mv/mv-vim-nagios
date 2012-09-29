# $Revision: 1.24 $, $Date: 2009/10/16 10:13:28 $
Summary:	Vim syntax: Nagios configuration files syntax
Summary(pl.UTF-8):	Opis skÅ‚adni dla Vima: podÅ›wietlanie skÅ‚adni dla plikÃ³w konfiguracyjnych Nagiosa
Name:		vim-syntax-nagios
Version:	1.20
Release:	1
Epoch:		1
License:	as-is
Group:		Applications/Editors/Vim
Source0:	nagios.vim
URL:		http://bugs.gentoo.org/show_bug.cgi?id=76712
Requires:	vim-rt >= 4:7.2.239-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles
%define		syntax		nagios

%description
This plugin provides syntax highlighting for Nagios configuration
files. Detection is by filename (/etc/nagios).

%description -l pl.UTF-8
Ta wtyczka dostarcza podÅ›wietlanie skÅ‚adni dla plikÃ³w konfiguracyjnych
Nagiosa. Pliki sÄ… rozpoznawane po nazwie (/etc/nagios).

%prep

%build
rev=$(awk '/^".*Revision:/{print $5}' %{SOURCE0})
if [ "$rev" != "%{version}" ]; then
	: Update version $rev, and retry
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,ftdetect}
cp -a %{SOURCE0} $RPM_BUILD_ROOT%{_vimdatadir}/syntax

cat > $RPM_BUILD_ROOT%{_vimdatadir}/ftdetect/%{syntax}.vim <<-EOF
au BufNewFile,BufRead /*etc/nagios/*.cfg,*sample-config/template-object/*.cfg{,.in},*/packages/nagios-plugin*/*.cfg,/var/lib/nagios/objects.*cache set filetype=%{syntax}
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/%{syntax}.vim
%{_vimdatadir}/ftdetect/%{syntax}.vim

%define date	%(echo `LC_ALL="C" date +"%a %b %d %Y"`)
%changelog
* %{date} PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org

$Log: vim-syntax-nagios.spec,v $
Revision 1.24  2009/10/16 10:13:28  glen
- v1.20: add escalation_period, escalation_options

Revision 1.23  2009/09/09 10:10:31  glen
- match *.cfg from nagios packages in cvs

Revision 1.22  2009/09/04 08:48:01  glen
- fix epoch

Revision 1.21  2009/09/04 08:47:44  glen
- up to 1.17

Revision 1.20  2008/06/08 10:03:50  glen
- updated to 1.5

Revision 1.19  2008-05-29 20:06:50  glen
- vimdatadir is in vim-rt package; rel 10

Revision 1.18  2007-02-12 22:09:19  glen
- tabs in preamble

Revision 1.17  2007/02/12 01:06:36  baggins
- converted to UTF-8

Revision 1.16  2005/09/16 20:40:50  glen
- rel 9

Revision 1.15  2005/07/18 15:34:40  glen
- source moved to PLD cvs
- use "set filetype" to get syntax applied unconditionally
- rel 8

Revision 1.14  2005/05/12 19:45:48  qboosh
- pl summary update

Revision 1.13  2005/05/12 19:39:39  glen
- cleanups

Revision 1.12  2005/05/12 19:31:59  glen
- unify with vim-syntax-ruby.spec

Revision 1.11  2005/05/08 17:32:18  glen
- detect objects.cache; rel 7

Revision 1.10  2005/05/08 15:48:03  glen
- add serviceextinfo block; rel 6

Revision 1.9  2005/05/03 12:01:55  glen
- failure_prediction_enabled from nagios 2.0
- rel 5

Revision 1.8  2005/04/09 18:07:32  glen
- rel 4; STBR

Revision 1.7  2005/03/06 21:41:52  glen
- updated Patch0
- added URL
- rel 3; STBR

Revision 1.6  2005/02/24 11:22:03  glen
- rel 2; STBR

Revision 1.5  2005/02/07 05:44:26  glen
- also set syntax inside nagios sourcecode

Revision 1.4  2005/02/04 00:20:13  glen
- rel 1
- STBR

Revision 1.3  2005/02/03 23:13:59  qboosh
- pl

Revision 1.2  2005/01/28 18:53:43  glen
- add few missing directives

Revision 1.1  2005/01/28 18:49:29  glen
- vim syntax for nagios configuration files

