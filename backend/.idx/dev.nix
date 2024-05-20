# https://developers.google.com/idx/guides/customize-idx-env
{ pkgs, ... }: {
  channel = "stable-23.11";

  packages = [
    pkgs.python310
    pkgs.python310Packages.pip
    pkgs.nodejs_18
    pkgs.poetry
    pkgs.just
    pkgs.docker
    pkgs.docker-compose
    pkgs.pipx
  ];

  env = { };
  idx = {
    # https://open-vsx.org/
    extensions = [
      # "vscodevim.vim"
      "vscode-icons-team.vscode-icons"
      "qwtel.sqlite-viewer"
      "charliermarsh.ruff"
    ];

    previews = {
      enable = true;
      previews = {
        # web = {
        #   # Example: run "npm run dev" with PORT set to IDX's defined port for previews,
        #   # and show it in IDX's web preview panel
        #   command = ["npm" "run" "dev"];
        #   manager = "web";
        #   env = {
        #     # Environment variables to set for your server
        #     PORT = "$PORT";
        #   };
        # };
      };
    };

    workspace = {
      onCreate = {
        # npm-install = 'npm install';
      };
      onStart = {
        # Example: start a background task to watch and re-build backend code
        # watch-backend = "npm run watch-backend";
      };
    };
  };
}
