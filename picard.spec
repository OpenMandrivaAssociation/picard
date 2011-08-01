Summary:	MusicBrainz-based audio tagger
Name:		picard
Version:	0.15.1
Release:	%mkrel 1
Group:		Sound
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv2+
Url:		http://musicbrainz.org/doc/PicardTagger
Source0:	http://ftp.musicbrainz.org/pub/musicbrainz/picard/%{name}-%{version}.tar.gz

Source1:	http://users.musicbrainz.org/~luks/picard-qt/plugins/discnumber.py
Source2:	http://users.musicbrainz.org/~luks/picard-qt/plugins/featartist.py
Source3:	http://users.musicbrainz.org/~luks/picard-qt/plugins/coverart.py
#gw old API:
#Source4:	http://dispuut-ivv.nl/~jan/bonusdisc.py
#http://users.musicbrainz.org/~luks/picard-qt/plugins/lastfm/
Source5:	lastfm.tar.bz2
Source6:	http://users.musicbrainz.org/~luks/picard-qt/plugins/addrelease.py
Source7:	http://users.musicbrainz.org/~luks/picard-qt/plugins/cuesheet.py
#gw old API:
#Source8:	http://foolip.org/mb/encoding.py
# search plugins
#gw they lag behind and support 0.9.0 only
#Source9:	SearchAMG.py
## actual URL http://wiki.musicbrainz.org/PicardQt/Plugins?action=AttachFile&do=get&target=SearchAMG.py

#Source10:	http://users.musicbrainz.org/~brianfreud/SearchDiscogs3.py
#Source11:	http://users.musicbrainz.org/~brianfreud/SearchAmazon3.py
#Source12:	http://users.musicbrainz.org/~brianfreud/SearchCastAlbums3.py
#Source13:	http://users.musicbrainz.org/~brianfreud/SearchFilmMusziek3.py
#Source14:	http://users.musicbrainz.org/~brianfreud/SearchGMR.py
#Source15:	http://users.musicbrainz.org/~brianfreud/SearchGoogle3.py
#Source16:	http://users.musicbrainz.org/~brianfreud/SearchLortelArchives3.py
#Source17:	http://users.musicbrainz.org/~brianfreud/SearchSoundtrackCollector3.py
#Source18:	http://users.musicbrainz.org/~brianfreud/SearchSoundtrackINFO3.py
#
Source19: http://users.musicbrainz.org/~luks/picard-plugins/open_in_gui.py
Source20: http://users.musicbrainz.org/~luks/picard-plugins/titlecase.py
Source21: http://users.musicbrainz.org/~luks/picard-plugins/release_type.py
Source22: http://users.musicbrainz.org/~luks/picard-plugins/featartistsintitles.py
Patch0:		picard-0.14-avutil-linking.patch
%py_requires -d
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
BuildRequires:	python-qt4-core >= 4.3
BuildRequires:	mutagen > 1.11
BuildRequires:	libofa-devel
BuildRequires:	libexpat-devel
BuildRequires:	libffmpeg-devel
Requires:	python-qt4-core >= 4.3
Requires:	python-qt4-gui >= 4.3
Requires:	python-qt4-network >= 4.3
Requires:	python-qt4-xml >= 4.3
Requires:	python-sip
Requires:	mutagen > 1.9
Requires:	libdiscid


%description
Picard is an audio tagging application using data from the MusicBrainz
database. The tagger is album or release oriented, rather than
track-oriented.

%prep
%setup -q -n %name-%version
%apply_patches

%build
env %{__python} setup.py config
env CFLAGS="%{optflags} -I%_includedir/libavcodec -I%_includedir/libavformat" %{__python} setup.py build

# (tpg) it fails for now
#%check
#%{__python} setup.py test

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}
install -D picard.desktop %buildroot%_datadir/applications/picard.desktop 
sed -i -e 's/^Icon=%{name}-32.png$/Icon=%{name}-32/g' %{buildroot}%{_datadir}/applications/*

desktop-file-install \
	--remove-category="Application" \
	--dir=%{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*
	

%define PLUGINDIR %{buildroot}%{python_sitearch}/picard/plugins/

install -pm 0644 %{SOURCE1} %{PLUGINDIR}
install -pm 0644 %{SOURCE2} %{PLUGINDIR}
install -pm 0644 %{SOURCE3} %{PLUGINDIR}
#install -pm 0644 %{SOURCE4} %{PLUGINDIR}
tar -xjf %{SOURCE5} -C %{PLUGINDIR}
install -pm 0644 %{SOURCE6} %{PLUGINDIR}
install -pm 0644 %{SOURCE7} %{PLUGINDIR}
#install -pm 0644 %{SOURCE8} %{PLUGINDIR}

#install -pm 0644 %{SOURCE10} %{PLUGINDIR}
#install -pm 0644 %{SOURCE11} %{PLUGINDIR}
#install -pm 0644 %{SOURCE12} %{PLUGINDIR}
#install -pm 0644 %{SOURCE13} %{PLUGINDIR}
#install -pm 0644 %{SOURCE14} %{PLUGINDIR}
#install -pm 0644 %{SOURCE15} %{PLUGINDIR}
#install -pm 0644 %{SOURCE16} %{PLUGINDIR}
#install -pm 0644 %{SOURCE17} %{PLUGINDIR}
#install -pm 0644 %{SOURCE18} %{PLUGINDIR}

install -pm 0644 %{SOURCE19} %{PLUGINDIR}
install -pm 0644 %{SOURCE20} %{PLUGINDIR}
install -pm 0644 %{SOURCE21} %{PLUGINDIR}
install -pm 0644 %{SOURCE22} %{PLUGINDIR}

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS.txt NEWS.txt INSTALL.txt
%{_bindir}/picard
%{_datadir}/applications/*.desktop
%_datadir/icons/hicolor/*/apps/picard.png
%{python_sitearch}/*egg-info
%dir %{python_sitearch}/picard
%{python_sitearch}/picard/*
