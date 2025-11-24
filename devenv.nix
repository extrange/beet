{
  config,
  pkgs,
  ...
}:

{
  languages.python = {
    enable = true;
    package = pkgs.python314;
    uv.enable = true;
    uv.sync.enable = true;
  };
  git-hooks.hooks = {
    trim-trailing-whitespace.enable = true;
    end-of-file-fixer.enable = true;
    check-yaml.enable = true; # Does not validate schema
    check-added-large-files.enable = true;
    check-case-conflicts.enable = true;
    actionlint.enable = true;
    trufflehog.enable = true;
  };
  enterShell = ''
    . ${config.env.DEVENV_STATE}/venv/bin/activate
  '';
}
