{ pkgs }: {
  deps = [
    pkgs.yakut
    pkgs.nodePackages.vscode-langservers-extracted
    pkgs.nodePackages.typescript-language-server
  ];
}