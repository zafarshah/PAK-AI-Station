# PAK-AI Station V0.1— Streamlit dashboard

## Fixes
- Photos are fetched independently per module from Wikimedia Commons using `python photos.py` **in Google Colab**, with license metadata saved beside each image. Review images and licenses before public launch. If none is found, a correctly labeled colored fallback is shown.
- Every photo is cropped to 960×600 and displayed at 16:10.
- Functional English/Urdu, dark/light, small/medium/large controls.
- Local SQLite login/register and 20 demonstration starter credits; AI text call charges one credit only after successful response.
- **Real-money payments are intentionally disabled**. Never collect payment without a verified Stripe webhook and proper hosted security infrastructure.
- Existing story content and approved-data retrieval preserved.

## Colab
Run: `%pip install -q "streamlit>=1.42,<2" "requests>=2.31,<3" "Pillow>=10,<13"`
Extract ZIP to `/content/PAK_AI_V07`, then `!cd /content/PAK_AI_V07 && python photos.py` (network required).
Set `GROQ_API_KEY`, `OPENAI_API_KEY`, `GEMINI_API_KEY` in Colab Secrets and copy to environment.
Run `streamlit run /content/PAK_AI_V07/app.py --server.port 8501 --server.address 0.0.0.0 --server.headless true --server.enableCORS false --server.enableXsrfProtection false` for **private Colab testing only**.
Use `output.serve_kernel_port_as_iframe(8501)`. Do not disable security protections on public hosting.

## Important
- The welcome image is the user-provided photograph; it may carry a watermark and requires rights review.
- Commons search can return imperfect matches; manually review each downloaded file and `.license.json` record.
- Colab SQLite accounts are ephemeral and not suitable for a public payment system. Deploy authentication, persistent database, HTTPS, rate limits, and verified Stripe checkout/webhooks before commercial release.
- Weather is sourced from Open-Meteo. Hotel prices, drivers, alerts and official records require separate verified data feeds.


## User-selected photo mappings
Eight supplied images have been mapped to their corresponding subjects: markets, grandma stories, kids learning, Quran, utilities/roads, forest/wildlife, agriculture/orchards, and tourism. All are normalized to 960x600 (16:10) using center cropping. The existing welcome image is unchanged. Public information, fisheries and environment require their own images; use `python photos.py` to download candidate images for missing modules, then review them before publishing. Do not run an image-replacement script over these curated images. Image rights remain to be confirmed before public deployment.
- `info.jpg`: regional map of Gilgit-Baltistan (Public Information)
- `env.jpg`: damaged bridge / flood impact (Environment & Disasters)
- `fishery.jpg`: fish-farming cages (Fisheries & Aquaculture)
- All three are 960 × 600 and assigned by the exact module IDs in `content.py`.
- The eight curated V0.8 images and original welcome image are preserved.
- **Important rights notice:** The disaster photo contains a Getty Images / Anadolu watermark. It is included solely for private prototype review; obtain a license or replace it with an authorized image before publishing. Rights to all supplied images must be confirmed.
- Do not run `photos.py` if you want to keep only the curated user-provided photos.
