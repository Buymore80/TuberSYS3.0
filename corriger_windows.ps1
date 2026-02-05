# Script de Correction pour Windows - TuberSYS 3.0

Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║   TuberSYS 3.0 - Correction pour Windows         ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Créer le dossier data s'il n'existe pas
Write-Host "📁 Création du dossier data..." -ForegroundColor Yellow
if (-not (Test-Path "data")) {
    New-Item -ItemType Directory -Path "data" | Out-Null
    Write-Host "✅ Dossier data créé" -ForegroundColor Green
} else {
    Write-Host "✅ Dossier data existe déjà" -ForegroundColor Green
}

# Créer le fichier .env avec le bon chemin Windows
Write-Host ""
Write-Host "📝 Configuration du fichier .env..." -ForegroundColor Yellow

$envContent = @"
# Configuration de l'application
SECRET_KEY=votre-cle-secrete-ultra-complexe-a-changer
DATABASE_PATH=data/tubersys.db
FLASK_ENV=development

# Pour partager la base de données entre plusieurs PC
# Décommentez et modifiez cette ligne pour utiliser un dossier partagé
# DATABASE_PATH=Z:/TuberSYS/data/tubersys.db  # Windows
# DATABASE_PATH=/mnt/shared/TuberSYS/data/tubersys.db  # Linux
"@

$envContent | Out-File -FilePath ".env" -Encoding UTF8
Write-Host "✅ Fichier .env créé avec chemin relatif" -ForegroundColor Green

# Initialiser la base de données
Write-Host ""
Write-Host "🔧 Initialisation de la base de données..." -ForegroundColor Yellow
Write-Host ""

python -c "from app import init_db; init_db()"

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "════════════════════════════════════════════════════" -ForegroundColor Green
    Write-Host "✅ CORRECTION TERMINÉE AVEC SUCCÈS !" -ForegroundColor Green
    Write-Host "════════════════════════════════════════════════════" -ForegroundColor Green
    Write-Host ""
    Write-Host "🚀 Vous pouvez maintenant lancer l'application :" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "   python app.py" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Puis ouvrez : http://localhost:5000" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "🔑 Connexion :" -ForegroundColor Cyan
    Write-Host "   Username: admin" -ForegroundColor Yellow
    Write-Host "   Password: admin123" -ForegroundColor Yellow
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "❌ Erreur lors de l'initialisation" -ForegroundColor Red
    Write-Host "Vérifiez que Python et toutes les dépendances sont installés" -ForegroundColor Yellow
}

Write-Host "Appuyez sur une touche pour continuer..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
