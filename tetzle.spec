Name:		tetzle
Version:	2.0.0
Release:	2
Summary:	Tetzle is a jigsaw puzzle game with tetrominoes
License:	GPLv3
Group:		Games/Puzzles
URL:		https://gottcode.org/tetzle/
Source:		%{name}-%{version}.tar.xz
BuildRequires:	qt4-devel

%description
A jigsaw puzzle game that uses tetrominoes for the pieces.
Any image can be imported and used to create puzzles with
a wide range of sizes. Games are saved automatically, and
you can select between currently in progress games.

%prep
%setup -q

%build
%qmake_qt4 PREFIX=%{_prefix}
%make

%install
%__rm -rf %{buildroot}
%__make install INSTALL_ROOT=%{buildroot}

%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Type=Application
Name=Tetzle
GenericName=Jigsaw Puzzle Game
GenericName[de]=Jigsaw Puzzle Spiel
Comment=Jigsaw puzzle with tetromino pieces
Comment[de]=Jigsaw Puzzle mit Tetromino Stücke
Icon=tetzle
Exec=tetzle
Terminal=false
Categories=Game;LogicGame;
EOF

%clean
%__rm -rf %{buildroot}

%files
%doc COPYING CREDITS ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/%{name}



%changelog
* Wed Mar 14 2012 Andrey Bondrov <abondrov@mandriva.org> 2.0.0-1mdv2011.0
+ Revision: 784974
- Fix summary
- imported package tetzle

