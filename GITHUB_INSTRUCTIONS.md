# 🚀 How to Push Your Portfolio to GitHub

Follow these steps to upload your `data-analyst-portfolio` to GitHub.

## 1. Create a Repository on GitHub
1.  Log in to your [GitHub](https://github.com/) account.
2.  Click the **+** icon in the top right and select **New repository**.
3.  **Repository name**: `data-analyst-portfolio` (or `portfolio`).
4.  **Description**: "Senior Data Analyst Portfolio (8+ Years) - SQL, Python, Excel, Power BI."
5.  **Public/Private**: Choose **Public** so recruiters can see it.
6.  **Initialize this repository with**: UNCHECK everything (Add a README, .gitignore, etc.) because we already have them locally.
7.  Click **Create repository**.
8.  Copy the HTTPS URL (e.g., `https://github.com/yourusername/data-analyst-portfolio.git`).

## 2. Initialize Git Locally (Terminal)
Open your terminal and run these commands one by one:

```bash
# Navigate to your portfolio folder
cd /Users/mac/Desktop/App/portfolio/data-analyst-portfolio

# Initialize Git
git init

# Add all files
git add .

# Commit your changes
git commit -m "Initial commit: Senior Data Analyst Portfolio with 8 projects"

# Rename branch to main (standard practice)
git branch -M main

# Link to your new GitHub repository (Replace URL below with YOURS)
git remote add origin https://github.com/yourusername/data-analyst-portfolio.git

# Push the files
git push -u origin main
```

## 3. Verify
Refresh your GitHub repository page. You should see all your folders, the beautiful `README.md` with flat UI screenshots, and your Senior CV in the `Documentation/` folder.

## ✅ Checklist for Success
- [ ] Did you fill in your details in `Documentation/Senior_CV.md`?
- [ ] Did you update the LinkedIn link in `README.md`?
