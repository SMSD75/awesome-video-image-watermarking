<div align="center">

<h1>Awesome Watermarking</h1>

<p><b>A curated list of watermarking research for images, video and audio — from classic deep watermarking to watermarks for diffusion and autoregressive generators, plus the attacks and benchmarks that test them.</b></p>

<a href="https://github.com/SMSD75/awesome-watermarking/pulls"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome"></a>
<img src="https://img.shields.io/badge/papers-82-blue.svg?style=flat-square" alt="Papers">
<img src="https://img.shields.io/badge/with%20code-46-orange.svg?style=flat-square" alt="With code">
<a href="https://github.com/SMSD75/awesome-watermarking/commits/main"><img src="https://img.shields.io/github/last-commit/SMSD75/awesome-watermarking?style=flat-square" alt="Last commit"></a>
<a href="LICENSE"><img src="https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg?style=flat-square" alt="License: CC0-1.0"></a>
<a href="https://github.com/SMSD75/awesome-watermarking/stargazers"><img src="https://img.shields.io/github/stars/SMSD75/awesome-watermarking?style=flat-square" alt="Stars"></a>

<br>

<img src="assets/overview.svg" alt="Overview of the watermarking pipeline and what this list covers" width="92%">

<p><b>Keywords:</b> <i>invisible watermarking · generative AI provenance · diffusion watermarking · video watermarking · audio watermarking · watermark removal · content authenticity</i></p>

<p><a href="#1-must-read-papers">Must-Read</a> · <a href="#2-paper-list">Paper List</a> · <a href="#3-papers-by-venue">By Venue</a> · <a href="#4-contributing">Contributing</a> · <a href="#5-citation">Citation</a></p>

</div>

## 🔥 News

- **[2026-10]** 🚀 Launched with 82 papers across image, video and audio watermarking, including the latest **CVPR 2026**, **ICLR 2026** and **AAAI 2026** work.
- **[2026-10]** 🎬 Video coverage spans post-hoc methods (Video Seal, WaTeRFlow) and in-generation methods for video diffusion (VideoShield, Safe-Sora, SIGMark, SPDMark).
- **[2026-10]** 🔊 Audio section added: AudioSeal, WavMark, Timbre watermarking, XAttnMark and AudioMarkBench.

> [!TIP]
> ⭐ marks foundational or highly influential work. Within each section, papers are ordered newest first. Contributions are welcome — see [Contributing](#4-contributing).

## 📑 Contents

- [1. Must-Read Papers](#1-must-read-papers)
- [2. Paper List](#2-paper-list)
  - [2.1 Foundations](#foundations)
  - [2.2 Image — Post-hoc Watermarking](#image-post-hoc)
  - [2.3 Image — In-Generation Watermarking](#image-in-generation)
    - [2.3.1 Fine-tuning / Weight-based](#fine-tuning--weight-based)
    - [2.3.2 Initial-noise / Semantic (Training-free)](#initial-noise--semantic)
    - [2.3.3 Autoregressive & Other Generators](#autoregressive--other-generators)
  - [2.4 Video Watermarking](#video)
    - [2.4.1 Post-hoc Video](#post-hoc-video)
    - [2.4.2 In-generation (Video Diffusion)](#in-generation-video-diffusion)
  - [2.5 Audio Watermarking](#audio)
  - [2.6 Attacks: Removal, Forgery & Spoofing](#attacks)
  - [2.7 Benchmarks, Surveys & Toolkits](#benchmarks)
- [3. Papers by Venue](#3-papers-by-venue)
- [4. Contributing](#4-contributing)
- [5. Citation](#5-citation)
- [Star History](#star-history)

## 1. Must-Read Papers

A starting point: the papers that defined each line of work.

| Title | Venue | Year | Code | Topic |
|:------|:-----:|:----:|:----:|:-----:|
| [**Secure Spread Spectrum Watermarking for Multimedia**](https://doi.org/10.1109/83.650120) | IEEE TIP | 1997 | — | Foundations |
| ![GitHub stars](https://img.shields.io/github/stars/ando-khachatryan/HiDDeN?style=social) <br> [**HiDDeN: Hiding Data With Deep Networks**](https://arxiv.org/abs/1807.09937) | ECCV | 2018 | [GitHub](https://github.com/ando-khachatryan/HiDDeN) | Foundations |
| ![GitHub stars](https://img.shields.io/github/stars/tancik/StegaStamp?style=social) <br> [**StegaStamp: Invisible Hyperlinks in Physical Photographs**](https://arxiv.org/abs/1904.05343) | CVPR | 2020 | [GitHub](https://github.com/tancik/StegaStamp) | Foundations |
| ![GitHub stars](https://img.shields.io/github/stars/ningyu1991/ArtificialGANFingerprints?style=social) <br> [**Artificial Fingerprinting for Generative Models: Rooting Deepfake Attribution in Training Data**](https://arxiv.org/abs/2007.08457) | ICCV | 2021 | [GitHub](https://github.com/ningyu1991/ArtificialGANFingerprints) | Foundations |
| ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/watermark-anything?style=social) <br> [**Watermark Anything with Localized Messages (WAM)**](https://arxiv.org/abs/2411.07231) | ICLR | 2025 | [GitHub](https://github.com/facebookresearch/watermark-anything) | Image · Post-hoc |
| [**SynthID-Image: Image Watermarking at Internet Scale**](https://arxiv.org/abs/2510.09263) | arXiv | 2025 | — | Image · Post-hoc |
| ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/stable_signature?style=social) <br> [**The Stable Signature: Rooting Watermarks in Latent Diffusion Models**](https://arxiv.org/abs/2303.15435) | ICCV | 2023 | [GitHub](https://github.com/facebookresearch/stable_signature) | Image · In-gen |
| ![GitHub stars](https://img.shields.io/github/stars/YuxinWenRick/tree-ring-watermark?style=social) <br> [**Tree-Ring Watermarks: Fingerprints for Diffusion Images that are Invisible and Robust**](https://arxiv.org/abs/2305.20030) | NeurIPS | 2023 | [GitHub](https://github.com/YuxinWenRick/tree-ring-watermark) | Image · In-gen |
| ![GitHub stars](https://img.shields.io/github/stars/bsmhmmlf/Gaussian-Shading?style=social) <br> [**Gaussian Shading: Provable Performance-Lossless Image Watermarking for Diffusion Models**](https://arxiv.org/abs/2404.04956) | CVPR | 2024 | [GitHub](https://github.com/bsmhmmlf/Gaussian-Shading) | Image · In-gen |
| ![GitHub stars](https://img.shields.io/github/stars/XuandongZhao/PRC-Watermark?style=social) <br> [**An Undetectable Watermark for Generative Image Models (PRC Watermark)**](https://arxiv.org/abs/2410.07369) | ICLR | 2025 | [GitHub](https://github.com/XuandongZhao/PRC-Watermark) | Image · In-gen |
| ![GitHub stars](https://img.shields.io/github/stars/DAI-Lab/RivaGAN?style=social) <br> [**RivaGAN: Robust Invisible Video Watermarking with Attention**](https://arxiv.org/abs/1909.01285) | arXiv | 2019 | [GitHub](https://github.com/DAI-Lab/RivaGAN) | Video |
| ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/videoseal?style=social) <br> [**Video Seal: Open and Efficient Video Watermarking**](https://arxiv.org/abs/2412.09492) | arXiv | 2024 | [GitHub](https://github.com/facebookresearch/videoseal) | Video |
| ![GitHub stars](https://img.shields.io/github/stars/hurunyi/VideoShield?style=social) <br> [**VideoShield: Regulating Diffusion-based Video Generation Models via Watermarking**](https://arxiv.org/abs/2501.14195) | ICLR | 2025 | [GitHub](https://github.com/hurunyi/VideoShield) | Video |
| ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/audioseal?style=social) <br> [**Proactive Detection of Voice Cloning with Localized Watermarking (AudioSeal)**](https://arxiv.org/abs/2401.17264) | ICML | 2024 | [GitHub](https://github.com/facebookresearch/audioseal) | Audio |
| ![GitHub stars](https://img.shields.io/github/stars/XuandongZhao/WatermarkAttacker?style=social) <br> [**Invisible Image Watermarks Are Provably Removable Using Generative AI**](https://arxiv.org/abs/2306.01953) | NeurIPS | 2024 | [GitHub](https://github.com/XuandongZhao/WatermarkAttacker) | Attack |
| ![GitHub stars](https://img.shields.io/github/stars/andrekassis/ai-watermark?style=social) <br> [**UnMarker: A Universal Attack on Defensive Image Watermarking**](https://arxiv.org/abs/2405.08363) | IEEE S&P | 2025 | [GitHub](https://github.com/andrekassis/ai-watermark) | Attack |
| ![GitHub stars](https://img.shields.io/github/stars/umd-huang-lab/WAVES?style=social) <br> [**WAVES: Benchmarking the Robustness of Image Watermarks**](https://arxiv.org/abs/2401.08573) | ICML | 2024 | [GitHub](https://github.com/umd-huang-lab/WAVES) | Benchmark |

## 2. Paper List

<a id="foundations"></a>

### 2.1 Foundations

+ ⭐ **Secure Spread Spectrum Watermarking for Multimedia** [[IEEE TIP 1997](https://doi.org/10.1109/83.650120)]
+ ⭐ **HiDDeN: Hiding Data With Deep Networks** [[ECCV 2018](https://arxiv.org/abs/1807.09937)] [[Code](https://github.com/ando-khachatryan/HiDDeN)] ![GitHub stars](https://img.shields.io/github/stars/ando-khachatryan/HiDDeN?style=social)
+ ⭐ **StegaStamp: Invisible Hyperlinks in Physical Photographs** [[CVPR 2020](https://arxiv.org/abs/1904.05343)] [[Code](https://github.com/tancik/StegaStamp)] ![GitHub stars](https://img.shields.io/github/stars/tancik/StegaStamp?style=social)
+ **Distortion Agnostic Deep Watermarking** [[CVPR 2020](https://arxiv.org/abs/2001.04580)]
+ ⭐ **Artificial Fingerprinting for Generative Models: Rooting Deepfake Attribution in Training Data** [[ICCV 2021](https://arxiv.org/abs/2007.08457)] [[Code](https://github.com/ningyu1991/ArtificialGANFingerprints)] ![GitHub stars](https://img.shields.io/github/stars/ningyu1991/ArtificialGANFingerprints?style=social)
+ **MBRS: Enhancing Robustness of DNN-based Watermarking by Mini-Batch of Real and Simulated JPEG Compression** [[ACM MM 2021](https://arxiv.org/abs/2108.08211)] [[Code](https://github.com/jzyustc/MBRS)] ![GitHub stars](https://img.shields.io/github/stars/jzyustc/MBRS?style=social)
+ **Watermarking Images in Self-Supervised Latent Spaces** [[ICASSP 2022](https://arxiv.org/abs/2112.09581)] [[Code](https://github.com/facebookresearch/ssl_watermarking)] ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/ssl_watermarking?style=social)

<p align="right"><a href="#-contents">⬆ back to top</a></p>

<a id="image-post-hoc"></a>

### 2.2 Image — Post-hoc Watermarking

+ **TrustMark: Robust Watermarking and Watermark Removal for Arbitrary Resolution Images** [[ICCV 2025](https://arxiv.org/abs/2311.18297)]
+ ⭐ **Watermark Anything with Localized Messages (WAM)** [[ICLR 2025](https://arxiv.org/abs/2411.07231)] [[Code](https://github.com/facebookresearch/watermark-anything)] ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/watermark-anything?style=social)
+ **Robust Watermarking Using Generative Priors Against Image Editing: From Benchmarking to Advances (VINE, W-Bench)** [[ICLR 2025](https://arxiv.org/abs/2410.18775)] [[Code](https://github.com/Shilin-LU/VINE)] ![GitHub stars](https://img.shields.io/github/stars/Shilin-LU/VINE?style=social)
+ **InvisMark: Invisible and Robust Watermarking for AI-generated Image Provenance** [[WACV 2025](https://arxiv.org/abs/2411.07795)] [[Code](https://github.com/microsoft/InvisMark)] ![GitHub stars](https://img.shields.io/github/stars/microsoft/InvisMark?style=social)
+ ⭐ **SynthID-Image: Image Watermarking at Internet Scale** [[arXiv 2025](https://arxiv.org/abs/2510.09263)]
+ **Pixel Seal: Adversarial-only Training for Invisible Image and Video Watermarking** [[arXiv 2025](https://arxiv.org/abs/2512.16874)] [[Code](https://github.com/facebookresearch/videoseal)] ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/videoseal?style=social)
+ **Attack-Resilient Image Watermarking Using Stable Diffusion (ZoDiac)** [[NeurIPS 2024](https://arxiv.org/abs/2401.04247)] [[Code](https://github.com/zhanglijun95/ZoDiac)] ![GitHub stars](https://img.shields.io/github/stars/zhanglijun95/ZoDiac?style=social)

<p align="right"><a href="#-contents">⬆ back to top</a></p>

<a id="image-in-generation"></a>

### 2.3 Image — In-Generation Watermarking

<a id="fine-tuning--weight-based"></a>

#### 2.3.1 Fine-tuning / Weight-based

+ **SleeperMark: Towards Robust Watermark against Fine-Tuning Text-to-image Diffusion Models** [[CVPR 2025](https://arxiv.org/abs/2412.04852)] [[Code](https://github.com/taco-group/SleeperMark)] ![GitHub stars](https://img.shields.io/github/stars/taco-group/SleeperMark?style=social)
+ **WMAdapter: Adding WaterMark Control to Latent Diffusion Models** [[ICML 2025](https://arxiv.org/abs/2406.08337)]
+ **WaterFlow: Learning Fast & Robust Watermarks using Stable Diffusion** [[ICLR 2025 Workshop](https://arxiv.org/abs/2504.12354)]
+ **SAT-LDM: Provably Generalizable Image Watermarking for Latent Diffusion Models with Self-Augmented Training** [[arXiv 2025](https://arxiv.org/abs/2501.00463)]
+ **WOUAF: Weight Modulation for User Attribution and Fingerprinting in Text-to-Image Diffusion Models** [[CVPR 2024](https://arxiv.org/abs/2306.04744)]
+ **AquaLoRA: Toward White-box Protection for Customized Stable Diffusion Models via Watermark LoRA** [[ICML 2024](https://arxiv.org/abs/2405.11135)] [[Code](https://github.com/Georgefwt/AquaLoRA)] ![GitHub stars](https://img.shields.io/github/stars/Georgefwt/AquaLoRA?style=social)
+ ⭐ **The Stable Signature: Rooting Watermarks in Latent Diffusion Models** [[ICCV 2023](https://arxiv.org/abs/2303.15435)] [[Code](https://github.com/facebookresearch/stable_signature)] ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/stable_signature?style=social)
+ **A Recipe for Watermarking Diffusion Models** [[arXiv 2023](https://arxiv.org/abs/2303.10137)] [[Code](https://github.com/yunqing-me/WatermarkDM)] ![GitHub stars](https://img.shields.io/github/stars/yunqing-me/WatermarkDM?style=social)

<a id="initial-noise--semantic"></a>

#### 2.3.2 Initial-noise / Semantic (Training-free)

+ **OptMark: Robust Multi-bit Diffusion Watermarking via Inference Time Optimization** [[AAAI 2026](https://arxiv.org/abs/2508.21727)] [[Project](https://jiazheng-xing.github.io/optmark-home)]
+ **Guidance Watermarking for Diffusion Models** [[ICLR 2026](https://arxiv.org/abs/2509.22126)]
+ **Spherical Watermark: Encryption-Free, Lossless Watermarking for Diffusion Models** [[ICLR 2026](https://openreview.net/forum?id=2eAGrunxVz)]
+ **MaxMark: High-Capacity Diffusion-Native Watermarking via Robust and Invertible Latent Embedding** [[CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Chang_MaxMark_High-Capacity_Diffusion-Native_Watermarking_via_Robust_and_Invertible_Latent_Embedding_CVPR_2026_paper.html)]
+ **Luminark: Training-free, Probabilistically-Certified Watermarking for General Vision Generative Models** [[arXiv 2026](https://arxiv.org/abs/2601.01085)]
+ ⭐ **An Undetectable Watermark for Generative Image Models (PRC Watermark)** [[ICLR 2025](https://arxiv.org/abs/2410.07369)] [[Code](https://github.com/XuandongZhao/PRC-Watermark)] ![GitHub stars](https://img.shields.io/github/stars/XuandongZhao/PRC-Watermark?style=social)
+ **Hidden in the Noise: Two-Stage Robust Watermarking for Images (WIND)** [[ICLR 2025](https://arxiv.org/abs/2412.04653)] [[Code](https://github.com/Kasraarabi/Hidden-in-the-Noise)] ![GitHub stars](https://img.shields.io/github/stars/Kasraarabi/Hidden-in-the-Noise?style=social)
+ **GaussMarker: Robust Dual-Domain Watermark for Diffusion Models** [[ICML 2025](https://arxiv.org/abs/2506.11444)]
+ **SEAL: Semantic Aware Image Watermarking** [[ICCV 2025](https://arxiv.org/abs/2503.12172)] [[Code](https://github.com/Kasraarabi/SEAL)] ![GitHub stars](https://img.shields.io/github/stars/Kasraarabi/SEAL?style=social)
+ **TAG-WM: Tamper-Aware Generative Image Watermarking via Diffusion Inversion Sensitivity** [[ICCV 2025](https://arxiv.org/abs/2506.23484)] [[Code](https://github.com/Suchenl/TAG-WM)] ![GitHub stars](https://img.shields.io/github/stars/Suchenl/TAG-WM?style=social)
+ **Shallow Diffuse: Robust and Invisible Watermarking through Low-Dimensional Subspaces in Diffusion Models** [[NeurIPS 2025](https://arxiv.org/abs/2410.21088)]
+ **MaXsive: High-Capacity and Robust Training-Free Generative Image Watermarking in Diffusion Models** [[ACM MM 2025](https://arxiv.org/abs/2507.21195)]
+ ⭐ **Gaussian Shading: Provable Performance-Lossless Image Watermarking for Diffusion Models** [[CVPR 2024](https://arxiv.org/abs/2404.04956)] [[Code](https://github.com/bsmhmmlf/Gaussian-Shading)] ![GitHub stars](https://img.shields.io/github/stars/bsmhmmlf/Gaussian-Shading?style=social)
+ **RingID: Rethinking Tree-Ring Watermarking for Enhanced Multi-Key Identification** [[ECCV 2024](https://arxiv.org/abs/2404.14055)] [[Code](https://github.com/showlab/RingID)] ![GitHub stars](https://img.shields.io/github/stars/showlab/RingID?style=social)
+ **ROBIN: Robust and Invisible Watermarks for Diffusion Models with Adversarial Optimization** [[NeurIPS 2024](https://arxiv.org/abs/2411.03862)] [[Code](https://github.com/Hannah1102/ROBIN)] ![GitHub stars](https://img.shields.io/github/stars/Hannah1102/ROBIN?style=social)
+ ⭐ **Tree-Ring Watermarks: Fingerprints for Diffusion Images that are Invisible and Robust** [[NeurIPS 2023](https://arxiv.org/abs/2305.20030)] [[Code](https://github.com/YuxinWenRick/tree-ring-watermark)] ![GitHub stars](https://img.shields.io/github/stars/YuxinWenRick/tree-ring-watermark?style=social)

<a id="autoregressive--other-generators"></a>

#### 2.3.3 Autoregressive & Other Generators

+ **Watermarking Autoregressive Image Generation** [[NeurIPS 2025](https://arxiv.org/abs/2506.16349)] [[Code](https://github.com/facebookresearch/wmar)] ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/wmar?style=social)
+ **A Watermark for Auto-Regressive Image Generation Models** [[arXiv 2025](https://arxiv.org/abs/2506.11371)]

<p align="right"><a href="#-contents">⬆ back to top</a></p>

<a id="video"></a>

### 2.4 Video Watermarking

<a id="post-hoc-video"></a>

#### 2.4.1 Post-hoc Video

+ **WaTeRFlow: Watermark Temporal Robustness via Flow Consistency** [[CVPR 2026](https://arxiv.org/abs/2512.19048)]
+ **Pixel Seal: Adversarial-only Training for Invisible Image and Video Watermarking** [[arXiv 2025](https://arxiv.org/abs/2512.16874)] [[Code](https://github.com/facebookresearch/videoseal)] ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/videoseal?style=social)
+ ⭐ **Video Seal: Open and Efficient Video Watermarking** [[arXiv 2024](https://arxiv.org/abs/2412.09492)] [[Code](https://github.com/facebookresearch/videoseal)] ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/videoseal?style=social)
+ **DVMark: A Deep Multiscale Framework for Video Watermarking** [[arXiv 2021 (Google)](https://arxiv.org/abs/2104.12734)]
+ ⭐ **RivaGAN: Robust Invisible Video Watermarking with Attention** [[arXiv 2019](https://arxiv.org/abs/1909.01285)] [[Code](https://github.com/DAI-Lab/RivaGAN)] ![GitHub stars](https://img.shields.io/github/stars/DAI-Lab/RivaGAN?style=social)

<a id="in-generation-video-diffusion"></a>

#### 2.4.2 In-generation (Video Diffusion)

+ **SPDMark: Selective Parameter Displacement for Robust Video Watermarking** [[CVPR 2026](https://arxiv.org/abs/2512.12090)]
+ **SIGMark: Scalable In-Generation Watermark with Blind Extraction for Video Diffusion** [[ICLR 2026](https://arxiv.org/abs/2603.02882)] [[Code](https://github.com/JeremyZhao1998/SIGMark-release)] ![GitHub stars](https://img.shields.io/github/stars/JeremyZhao1998/SIGMark-release?style=social)
+ **SKeDA: A Generative Watermarking Framework for Text-to-video Diffusion Models** [[arXiv 2026](https://arxiv.org/abs/2603.00194)]
+ ⭐ **VideoShield: Regulating Diffusion-based Video Generation Models via Watermarking** [[ICLR 2025](https://arxiv.org/abs/2501.14195)] [[Code](https://github.com/hurunyi/VideoShield)] ![GitHub stars](https://img.shields.io/github/stars/hurunyi/VideoShield?style=social)
+ **Safe-Sora: Safe Text-to-Video Generation via Graphical Watermarking** [[NeurIPS 2025](https://arxiv.org/abs/2505.12667)] [[Code](https://github.com/Sugewud/Safe-Sora)] ![GitHub stars](https://img.shields.io/github/stars/Sugewud/Safe-Sora?style=social)
+ **VideoMark: A Distortion-Free Robust Watermarking Framework for Video Diffusion Models** [[arXiv 2025](https://arxiv.org/abs/2504.16359)] [[Code](https://github.com/KYRIE-LI11/VideoMark)] ![GitHub stars](https://img.shields.io/github/stars/KYRIE-LI11/VideoMark?style=social)
+ **VidStamp: A Temporally-Aware Watermark for Ownership and Integrity in Video Diffusion Models** [[arXiv 2025](https://arxiv.org/abs/2505.01406)] [[Code](https://github.com/SPIN-UMass/VidStamp)] ![GitHub stars](https://img.shields.io/github/stars/SPIN-UMass/VidStamp?style=social)
+ **Video Signature: Implicit Watermarking for Video Diffusion Models (VidSig)** [[arXiv 2025](https://arxiv.org/abs/2506.00652)]
+ **I2VWM: Robust Watermarking for Image to Video Generation** [[arXiv 2025](https://arxiv.org/abs/2509.17773)]
+ **LVMark: Robust Watermark for Latent Video Diffusion Models** [[arXiv 2024](https://arxiv.org/abs/2412.09122)]

<p align="right"><a href="#-contents">⬆ back to top</a></p>

<a id="audio"></a>

### 2.5 Audio Watermarking

+ **Latent Watermarking of Audio Generative Models** [[ICASSP 2025](https://arxiv.org/abs/2409.02915)]
+ **XAttnMark: Learning Robust Audio Watermarking with Cross-Attention** [[ICML 2025](https://arxiv.org/abs/2502.04230)]
+ **SoK: How Robust is Audio Watermarking in Generative AI Models?** [[arXiv 2025](https://arxiv.org/abs/2503.19176)]
+ **Collaborative Watermarking for Adversarial Speech Synthesis** [[ICASSP 2024](https://arxiv.org/abs/2309.15224)]
+ **Detecting Voice Cloning Attacks via Timbre Watermarking** [[NDSS 2024](https://arxiv.org/abs/2312.03410)] [[Code](https://github.com/TimbreWatermarking/TimbreWatermarking)] ![GitHub stars](https://img.shields.io/github/stars/TimbreWatermarking/TimbreWatermarking?style=social)
+ ⭐ **Proactive Detection of Voice Cloning with Localized Watermarking (AudioSeal)** [[ICML 2024](https://arxiv.org/abs/2401.17264)] [[Code](https://github.com/facebookresearch/audioseal)] ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/audioseal?style=social)
+ **SilentCipher: Deep Audio Watermarking** [[Interspeech 2024](https://arxiv.org/abs/2406.03822)] [[Code](https://github.com/sony/silentcipher)] ![GitHub stars](https://img.shields.io/github/stars/sony/silentcipher?style=social)
+ **AudioMarkBench: Benchmarking Robustness of Audio Watermarking** [[NeurIPS 2024 (D&B)](https://arxiv.org/abs/2406.06979)]
+ **WavMark: Watermarking for Audio Generation** [[arXiv 2023](https://arxiv.org/abs/2308.12770)] [[Code](https://github.com/wavmark/wavmark)] ![GitHub stars](https://img.shields.io/github/stars/wavmark/wavmark?style=social)

<p align="right"><a href="#-contents">⬆ back to top</a></p>

<a id="attacks"></a>

### 2.6 Attacks: Removal, Forgery & Spoofing

+ **SHIFT: Stochastic Hidden-Trajectory Deflection for Removing Diffusion-based Watermark** [[arXiv 2026](https://arxiv.org/abs/2603.29742)] [[Code](https://github.com/ZhengGao-30/SHIFT-Watermark-Attack)] ![GitHub stars](https://img.shields.io/github/stars/ZhengGao-30/SHIFT-Watermark-Attack?style=social)
+ **MarkNull: Model-Agnostic Watermark Removal in AI-Generated Images via On-Manifold Latent Manipulation** [[arXiv 2026](https://arxiv.org/abs/2608.10166)]
+ ⭐ **UnMarker: A Universal Attack on Defensive Image Watermarking** [[IEEE S&P 2025](https://arxiv.org/abs/2405.08363)] [[Code](https://github.com/andrekassis/ai-watermark)] ![GitHub stars](https://img.shields.io/github/stars/andrekassis/ai-watermark?style=social)
+ **Image Watermarks are Removable Using Controllable Regeneration from Clean Noise (CtrlRegen)** [[ICLR 2025](https://arxiv.org/abs/2410.05470)] [[Code](https://github.com/yepengliu/CtrlRegen)] ![GitHub stars](https://img.shields.io/github/stars/yepengliu/CtrlRegen?style=social)
+ **A Transfer Attack to Image Watermarks** [[ICLR 2025](https://arxiv.org/abs/2403.15365)] [[Code](https://github.com/hifi-hyp/Watermark-Transfer-Attack)] ![GitHub stars](https://img.shields.io/github/stars/hifi-hyp/Watermark-Transfer-Attack?style=social)
+ **Black-Box Forgery Attacks on Semantic Watermarks for Diffusion Models** [[CVPR 2025](https://arxiv.org/abs/2412.03283)] [[Code](https://github.com/and-mill/semantic-forgery)] ![GitHub stars](https://img.shields.io/github/stars/and-mill/semantic-forgery?style=social)
+ **Forging and Removing Latent-Noise Diffusion Watermarks Using a Single Image** [[arXiv 2025](https://arxiv.org/abs/2504.20111)] [[Code](https://github.com/anubhav1997/watermark_forgery_removal)] ![GitHub stars](https://img.shields.io/github/stars/anubhav1997/watermark_forgery_removal?style=social)
+ **Robustness of AI-Image Detectors: Fundamental Limits and Practical Attacks** [[ICLR 2024](https://arxiv.org/abs/2310.00076)]
+ **Leveraging Optimization for Adaptive Attacks on Image Watermarks** [[ICLR 2024](https://arxiv.org/abs/2309.16952)]
+ ⭐ **Invisible Image Watermarks Are Provably Removable Using Generative AI** [[NeurIPS 2024](https://arxiv.org/abs/2306.01953)] [[Code](https://github.com/XuandongZhao/WatermarkAttacker)] ![GitHub stars](https://img.shields.io/github/stars/XuandongZhao/WatermarkAttacker?style=social)
+ **Can Simple Averaging Defeat Modern Watermarks?** [[NeurIPS 2024](https://arxiv.org/abs/2406.09026)] [[Code](https://github.com/showlab/watermark-steganalysis)] ![GitHub stars](https://img.shields.io/github/stars/showlab/watermark-steganalysis?style=social)
+ **Stable Signature is Unstable: Removing Image Watermark from Diffusion Models** [[arXiv 2024](https://arxiv.org/abs/2405.07145)]
+ **Evading Watermark based Detection of AI-Generated Content** [[CCS 2023](https://arxiv.org/abs/2305.03807)]

<p align="right"><a href="#-contents">⬆ back to top</a></p>

<a id="benchmarks"></a>

### 2.7 Benchmarks, Surveys & Toolkits

+ **MarkDiffusion: An Open-Source Toolkit for Generative Watermarking of Latent Diffusion Models** [[JMLR 2026](https://arxiv.org/abs/2509.10569)] [[Code](https://github.com/THU-BPM/MarkDiffusion)] ![GitHub stars](https://img.shields.io/github/stars/THU-BPM/MarkDiffusion?style=social)
+ **Erasing the Invisible: The 2024 NeurIPS Competition on Stress Testing Image Watermarks (Technical Report)** [[NeurIPS 2025 (D&B)](https://openreview.net/forum?id=BeFjjyzWOJ)]
+ **VideoMarkBench: Benchmarking Robustness of Video Watermarking** [[arXiv 2025](https://arxiv.org/abs/2505.21620)] [[Code](https://github.com/zhengyuan-jiang/VideoMarkBench)] ![GitHub stars](https://img.shields.io/github/stars/zhengyuan-jiang/VideoMarkBench?style=social)
+ **Detection Limits and Statistical Separability of Tree Ring Watermarks in Rectified Flow-based Text-to-Image Generation Models** [[arXiv 2025](https://arxiv.org/abs/2504.03850)] [[Code](https://github.com/dsgiitr/flux-watermarking)] ![GitHub stars](https://img.shields.io/github/stars/dsgiitr/flux-watermarking?style=social)
+ ⭐ **WAVES: Benchmarking the Robustness of Image Watermarks** [[ICML 2024](https://arxiv.org/abs/2401.08573)] [[Code](https://github.com/umd-huang-lab/WAVES)] ![GitHub stars](https://img.shields.io/github/stars/umd-huang-lab/WAVES?style=social)
+ **SoK: Watermarking for AI-Generated Content** [[arXiv 2024](https://arxiv.org/abs/2411.18479)]

<p align="right"><a href="#-contents">⬆ back to top</a></p>

## 3. Papers by Venue

Top-tier conference and journal papers from 2024 onward, grouped by venue. Click to expand.

<details>
<summary><b>CVPR 2026</b> (3)</summary>

+ [MaxMark: High-Capacity Diffusion-Native Watermarking via Robust and Invertible Latent Embedding](https://openaccess.thecvf.com/content/CVPR2026/html/Chang_MaxMark_High-Capacity_Diffusion-Native_Watermarking_via_Robust_and_Invertible_Latent_Embedding_CVPR_2026_paper.html) — *Image · In-gen*
+ [WaTeRFlow: Watermark Temporal Robustness via Flow Consistency](https://arxiv.org/abs/2512.19048) — *Video*
+ [SPDMark: Selective Parameter Displacement for Robust Video Watermarking](https://arxiv.org/abs/2512.12090) — *Video*

</details>

<details>
<summary><b>ICLR 2026</b> (3)</summary>

+ [Guidance Watermarking for Diffusion Models](https://arxiv.org/abs/2509.22126) — *Image · In-gen*
+ [Spherical Watermark: Encryption-Free, Lossless Watermarking for Diffusion Models](https://openreview.net/forum?id=2eAGrunxVz) — *Image · In-gen*
+ [SIGMark: Scalable In-Generation Watermark with Blind Extraction for Video Diffusion](https://arxiv.org/abs/2603.02882) [[Code](https://github.com/JeremyZhao1998/SIGMark-release)] — *Video*

</details>

<details>
<summary><b>AAAI 2026</b> (1)</summary>

+ [OptMark: Robust Multi-bit Diffusion Watermarking via Inference Time Optimization](https://arxiv.org/abs/2508.21727) — *Image · In-gen*

</details>

<details>
<summary><b>JMLR 2026</b> (1)</summary>

+ [MarkDiffusion: An Open-Source Toolkit for Generative Watermarking of Latent Diffusion Models](https://arxiv.org/abs/2509.10569) [[Code](https://github.com/THU-BPM/MarkDiffusion)] — *Benchmark*

</details>

<details>
<summary><b>CVPR 2025</b> (2)</summary>

+ [SleeperMark: Towards Robust Watermark against Fine-Tuning Text-to-image Diffusion Models](https://arxiv.org/abs/2412.04852) [[Code](https://github.com/taco-group/SleeperMark)] — *Image · In-gen*
+ [Black-Box Forgery Attacks on Semantic Watermarks for Diffusion Models](https://arxiv.org/abs/2412.03283) [[Code](https://github.com/and-mill/semantic-forgery)] — *Attack*

</details>

<details>
<summary><b>ICCV 2025</b> (3)</summary>

+ [TrustMark: Robust Watermarking and Watermark Removal for Arbitrary Resolution Images](https://arxiv.org/abs/2311.18297) — *Image · Post-hoc*
+ [SEAL: Semantic Aware Image Watermarking](https://arxiv.org/abs/2503.12172) [[Code](https://github.com/Kasraarabi/SEAL)] — *Image · In-gen*
+ [TAG-WM: Tamper-Aware Generative Image Watermarking via Diffusion Inversion Sensitivity](https://arxiv.org/abs/2506.23484) [[Code](https://github.com/Suchenl/TAG-WM)] — *Image · In-gen*

</details>

<details>
<summary><b>NeurIPS 2025</b> (4)</summary>

+ [Shallow Diffuse: Robust and Invisible Watermarking through Low-Dimensional Subspaces in Diffusion Models](https://arxiv.org/abs/2410.21088) — *Image · In-gen*
+ [Watermarking Autoregressive Image Generation](https://arxiv.org/abs/2506.16349) [[Code](https://github.com/facebookresearch/wmar)] — *Image · In-gen*
+ [Safe-Sora: Safe Text-to-Video Generation via Graphical Watermarking](https://arxiv.org/abs/2505.12667) [[Code](https://github.com/Sugewud/Safe-Sora)] — *Video*
+ [Erasing the Invisible: The 2024 NeurIPS Competition on Stress Testing Image Watermarks (Technical Report)](https://openreview.net/forum?id=BeFjjyzWOJ) — *Benchmark*

</details>

<details>
<summary><b>ICLR 2025</b> (7)</summary>

+ [Watermark Anything with Localized Messages (WAM)](https://arxiv.org/abs/2411.07231) [[Code](https://github.com/facebookresearch/watermark-anything)] — *Image · Post-hoc*
+ [Robust Watermarking Using Generative Priors Against Image Editing: From Benchmarking to Advances (VINE, W-Bench)](https://arxiv.org/abs/2410.18775) [[Code](https://github.com/Shilin-LU/VINE)] — *Image · Post-hoc*
+ [An Undetectable Watermark for Generative Image Models (PRC Watermark)](https://arxiv.org/abs/2410.07369) [[Code](https://github.com/XuandongZhao/PRC-Watermark)] — *Image · In-gen*
+ [Hidden in the Noise: Two-Stage Robust Watermarking for Images (WIND)](https://arxiv.org/abs/2412.04653) [[Code](https://github.com/Kasraarabi/Hidden-in-the-Noise)] — *Image · In-gen*
+ [VideoShield: Regulating Diffusion-based Video Generation Models via Watermarking](https://arxiv.org/abs/2501.14195) [[Code](https://github.com/hurunyi/VideoShield)] — *Video*
+ [Image Watermarks are Removable Using Controllable Regeneration from Clean Noise (CtrlRegen)](https://arxiv.org/abs/2410.05470) [[Code](https://github.com/yepengliu/CtrlRegen)] — *Attack*
+ [A Transfer Attack to Image Watermarks](https://arxiv.org/abs/2403.15365) [[Code](https://github.com/hifi-hyp/Watermark-Transfer-Attack)] — *Attack*

</details>

<details>
<summary><b>ICML 2025</b> (3)</summary>

+ [WMAdapter: Adding WaterMark Control to Latent Diffusion Models](https://arxiv.org/abs/2406.08337) — *Image · In-gen*
+ [GaussMarker: Robust Dual-Domain Watermark for Diffusion Models](https://arxiv.org/abs/2506.11444) — *Image · In-gen*
+ [XAttnMark: Learning Robust Audio Watermarking with Cross-Attention](https://arxiv.org/abs/2502.04230) — *Audio*

</details>

<details>
<summary><b>ACM MM 2025</b> (1)</summary>

+ [MaXsive: High-Capacity and Robust Training-Free Generative Image Watermarking in Diffusion Models](https://arxiv.org/abs/2507.21195) — *Image · In-gen*

</details>

<details>
<summary><b>IEEE S&P 2025</b> (1)</summary>

+ [UnMarker: A Universal Attack on Defensive Image Watermarking](https://arxiv.org/abs/2405.08363) [[Code](https://github.com/andrekassis/ai-watermark)] — *Attack*

</details>

<details>
<summary><b>WACV 2025</b> (1)</summary>

+ [InvisMark: Invisible and Robust Watermarking for AI-generated Image Provenance](https://arxiv.org/abs/2411.07795) [[Code](https://github.com/microsoft/InvisMark)] — *Image · Post-hoc*

</details>

<details>
<summary><b>ICASSP 2025</b> (1)</summary>

+ [Latent Watermarking of Audio Generative Models](https://arxiv.org/abs/2409.02915) — *Audio*

</details>

<details>
<summary><b>CVPR 2024</b> (2)</summary>

+ [WOUAF: Weight Modulation for User Attribution and Fingerprinting in Text-to-Image Diffusion Models](https://arxiv.org/abs/2306.04744) — *Image · In-gen*
+ [Gaussian Shading: Provable Performance-Lossless Image Watermarking for Diffusion Models](https://arxiv.org/abs/2404.04956) [[Code](https://github.com/bsmhmmlf/Gaussian-Shading)] — *Image · In-gen*

</details>

<details>
<summary><b>ECCV 2024</b> (1)</summary>

+ [RingID: Rethinking Tree-Ring Watermarking for Enhanced Multi-Key Identification](https://arxiv.org/abs/2404.14055) [[Code](https://github.com/showlab/RingID)] — *Image · In-gen*

</details>

<details>
<summary><b>NeurIPS 2024</b> (5)</summary>

+ [Attack-Resilient Image Watermarking Using Stable Diffusion (ZoDiac)](https://arxiv.org/abs/2401.04247) [[Code](https://github.com/zhanglijun95/ZoDiac)] — *Image · Post-hoc*
+ [ROBIN: Robust and Invisible Watermarks for Diffusion Models with Adversarial Optimization](https://arxiv.org/abs/2411.03862) [[Code](https://github.com/Hannah1102/ROBIN)] — *Image · In-gen*
+ [AudioMarkBench: Benchmarking Robustness of Audio Watermarking](https://arxiv.org/abs/2406.06979) — *Audio*
+ [Invisible Image Watermarks Are Provably Removable Using Generative AI](https://arxiv.org/abs/2306.01953) [[Code](https://github.com/XuandongZhao/WatermarkAttacker)] — *Attack*
+ [Can Simple Averaging Defeat Modern Watermarks?](https://arxiv.org/abs/2406.09026) [[Code](https://github.com/showlab/watermark-steganalysis)] — *Attack*

</details>

<details>
<summary><b>ICLR 2024</b> (2)</summary>

+ [Robustness of AI-Image Detectors: Fundamental Limits and Practical Attacks](https://arxiv.org/abs/2310.00076) — *Attack*
+ [Leveraging Optimization for Adaptive Attacks on Image Watermarks](https://arxiv.org/abs/2309.16952) — *Attack*

</details>

<details>
<summary><b>ICML 2024</b> (3)</summary>

+ [AquaLoRA: Toward White-box Protection for Customized Stable Diffusion Models via Watermark LoRA](https://arxiv.org/abs/2405.11135) [[Code](https://github.com/Georgefwt/AquaLoRA)] — *Image · In-gen*
+ [Proactive Detection of Voice Cloning with Localized Watermarking (AudioSeal)](https://arxiv.org/abs/2401.17264) [[Code](https://github.com/facebookresearch/audioseal)] — *Audio*
+ [WAVES: Benchmarking the Robustness of Image Watermarks](https://arxiv.org/abs/2401.08573) [[Code](https://github.com/umd-huang-lab/WAVES)] — *Benchmark*

</details>

<details>
<summary><b>NDSS 2024</b> (1)</summary>

+ [Detecting Voice Cloning Attacks via Timbre Watermarking](https://arxiv.org/abs/2312.03410) [[Code](https://github.com/TimbreWatermarking/TimbreWatermarking)] — *Audio*

</details>

<details>
<summary><b>ICASSP 2024</b> (1)</summary>

+ [Collaborative Watermarking for Adversarial Speech Synthesis](https://arxiv.org/abs/2309.15224) — *Audio*

</details>

<details>
<summary><b>Interspeech 2024</b> (1)</summary>

+ [SilentCipher: Deep Audio Watermarking](https://arxiv.org/abs/2406.03822) [[Code](https://github.com/sony/silentcipher)] — *Audio*

</details>

## 4. Contributing

Contributions are very welcome. To add a paper, open a pull request or an issue with:

```markdown
+ **Paper Title** [[Venue Year](paper_link)] [[Code](code_link)]
```

The README is generated from [`papers.json`](papers.json): add an entry there and run `python tools/build_readme.py`. Please keep to image, video and audio watermarking, prefer peer-reviewed versions, and link the arXiv or official proceedings page.

## 5. Citation

If you find this list useful, please consider starring ⭐ the repo and citing it:

```bibtex
@misc{salehi2026awesomewatermarking,
  title        = {Awesome Watermarking: A Curated List of Image, Video and Audio Watermarking Research},
  author       = {Salehi, Mohammadreza},
  year         = {2026},
  howpublished = {\url{https://github.com/SMSD75/awesome-watermarking}}
}
```

## Star History

<a href="https://star-history.com/#SMSD75/awesome-watermarking&Date">
  <img src="https://api.star-history.com/svg?repos=SMSD75/awesome-watermarking&type=Date" alt="Star History Chart" width="600">
</a>

<p align="right"><a href="#-contents">⬆ back to top</a></p>
