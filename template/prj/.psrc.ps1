$localenv = ".\.venv\Scripts\Activate.ps1"
if (Test-Path $localenv) {
    $localenv
} else {
    poetry env activate
}
