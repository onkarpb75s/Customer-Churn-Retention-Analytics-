# GitHub Upload Guide

## Important

Upload the **contents of this folder**, not the ZIP file itself.

Your GitHub repository should look like:

```text
customer-churn-retention-analytics/
├── README.md
├── dashboard.py
├── requirements.txt
├── data/
├── screenshots/
│   ├── customer_churn_dashboard.png
│   ├── churn_by_contract.png
│   ├── churn_by_internet.png
│   └── churn_by_tenure.png
├── reports/
├── sql/
└── src/
```

The `README.md` uses relative image paths such as:

```markdown
![Customer Churn Dashboard](./screenshots/customer_churn_dashboard.png)
```

GitHub will display the image automatically once both `README.md` and the `screenshots` folder are uploaded.

### If using GitHub's website

1. Create/open your repository.
2. Click **Add file → Upload files**.
3. Upload the folders/files from this project.
4. Make sure the `screenshots` folder and its PNG files are uploaded.
5. Commit the changes.
6. Open `README.md`.
7. The screenshots should appear automatically.

Do not upload only `README.md`; the image files must also be in the repository.
