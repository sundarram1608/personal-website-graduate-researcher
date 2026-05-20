import streamlit as st
from pathlib import Path
import base64
from PIL import Image

# -----------------------------
# INITIALIZING BASE DIRECTORY
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

# img_path = BASE_DIR / "images" / "pageicon.png"
# icon = Image.open(img_path)

st.set_page_config(page_title="Sundar Ram Subramanian: Portfolio", layout="wide") 



st.markdown(
            """
            <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
            """,
            unsafe_allow_html=True,
        )

# -----------------------------
# HEADER NAVIGATION
# -----------------------------
st.markdown(
            """
            <style>
              /* Remove Streamlit's default top padding so our bar can sit at the very top */
              .block-container { padding-top: 4.8rem !important; }

              /* Hide Streamlit's own top header bar so it doesn't push our nav down */
              /*[data-testid="stHeader"] { display: none; }*/
              
              [data-testid="stToolbar"] { display: none; } /* optional; removes the floating toolbar */
              

              /* Fixed nav bar at absolute top */
              .top-nav-wrap{
                              position: fixed;
                              top: 0;                 /* <-- RIGHT AT THE TOP */
                              left: 0;
                              right: 0;
                              z-index: 999999;
                              background: color(srgb 0.057 0.067 0.0882);
                              border-bottom: 1px solid rgba(54,82,102,0.12);
                              padding: 1px 1px;
                              width: 100%;
                              display: flex;
                            }

              /* Branding on the left */
              .top-nav-brand{
                              display: flex;
                              justify-content: flex-start; /* LEFT */
                              gap: 20px;
                              align-items: initial;
                              max-width: 1300px;
                              margin-left: 50px;
                              font-size: 1rem;
                              font-weight: 500;
                              width: 50%;
                            }

              .top-nav-links{
                              display: flex;
                              justify-content: flex-end; /* RIGHT */
                              gap: 20px;
                              align-items: center;
                              max-width: 1300px;
                              margin-right: 50px;
                              font-size: 0.9rem;
                              font-weight: 350;
                              width: 50%;
                            }

              /* Blue links, no underline */
              .top-nav-links a{
                                  color: #fcfcfc;
                                  text-decoration: none !important;
                                }
              .top-nav-links a:hover{
                                        text-decoration: none;
                                        color: #f5c542;
                                      }

              /* Prevent anchor jumps from hiding headings under the fixed nav */
              h2 { scroll-margin-top: 150px; }
              
                /* Branding on the right */
              .brand{
                      margin-left: 18px;          /* spacing from links */
                      font-weight: 700;
                      letter-spacing: 0.08em;
                      color: #ffffff;
                      font-size: 1.05rem;
                      padding: 6px 10px;
                      user-select: none;
                    }
                    
              .brand:hover {
                            background: rgba(255, 255, 255, 0.15);
                          }
              .highlight-name {
                                background: -webkit-linear-gradient(30deg, #3b82f6, #14b8a6);
                                -webkit-background-clip: text;
                                -webkit-text-fill-color: transparent;
                                }
                                
              /* Gradient button style */
              .cta-button {
                            display: inline-block;
                            padding: 14px 28px;
                            margin: 20px 12px 0 12px;
                            font-size: 1.1rem;
                            font-weight: 600;
                            text-decoration: none !important;

                            /* Button background */
                            background: linear-gradient(45deg, #3b82f6, #14b8a6);
                            border-radius: 10px;

                            /* FORCE white text */
                            color: #ffffff !important;
                            -webkit-text-fill-color: #ffffff !important;

                            transition: transform 0.2s ease, box-shadow 0.2s ease;
                          }

              .cta-button:hover {
                                  transform: translateY(-2px);
                                  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
                                }
              /* button style for resume */
              .cta-button-resume {
                                    display: inline-block;
                                    padding: 14px 28px;
                                    margin: 20px 12px 0 12px;
                                    font-size: 1.1rem;
                                    font-weight: 600;
                                    text-decoration: none !important;
        
                                    /* Button background */
                                    background: transparent;
                                    border-radius: 10px;
                                    border: 1.5px solid #9ca3af;
        
                                    /* FORCE white text */
                                    color: #ffffff !important;
                                    -webkit-text-fill-color: #ffffff !important;
        
                                    transition: transform 0.2s ease, box-shadow 0.2s ease;
                                  }

              .cta-button-resume:hover {
                                          transform: translateY(-2px);
                                          box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
                                          background: #f5c542;
                                        }

/* --- Two-column timeline container spacing --- */
              .timeline-title{
                                font-size: 1.4rem;
                                font-weight: 650;
                                margin: 0 0 14px 0;
                                    color: #fcfcfc;
                                    text-align: center;
                                  }
              /* --- Timeline base --- */
              .timeline{
                          position: relative;
                          padding-left: 24px; /* space for the line + dots */
                          margin-top: 6px;
                        }



              /* --- Each item --- */
              .t-item{
                        position: relative;
                        margin: 0 120px 20px 120px;
                        padding: 14px 14px 14px 16px;
                        background: transparent;
                        border: 1px solid rgba(255,255,255,0.12);
                        border-radius: 14px;
                        backdrop-filter: blur(8px);
                        -webkit-backdrop-filter: blur(8px);
                      }

            /* Academic badge dot (glow ring + gradient inner + white cap icon) */
              .t-item.academic:before{
                                        content: "";
                                        position: absolute;
                                        left: -39px;
                                        top: 14px;
                                        width: 25px;
                                        height: 25px;
                                        border-radius: 999px;

                                        /* 🔑 MULTI-LAYER BACKGROUND (icon on top, gradient below) */
                                        background:
                                          url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='white'%3E%3Cpath d='M12 3 1 9l11 6 9-4.91V17h2V9L12 3zm-6.5 9.09V16c0 1.66 3.13 3 6.5 3s6.5-1.34 6.5-3v-3.91L12 16l-6.5-3.91z'/%3E%3C/svg%3E")
                                            center / 20px 20px no-repeat,
                                          linear-gradient(45deg, #3b82f6, #14b8a6);

                                        /* subtle depth (your preferred look) */
                                        box-shadow:
                                          0 0 0 8px rgba(59,130,246,0.20),
                                          0 0 10px rgba(20,184,166,0.35);
                                      }
            
              /* Work badge dot */
              .t-item.work:before{
                                    content: "";
                                    position: absolute;
                                    left: -39px;
                                    top: 14px;
                                    width: 25px;
                                    height: 25px;
                                    border-radius: 999px;

                                    /* 🔑 MULTI-LAYER BACKGROUND (icon on top, gradient below) */
                                    background:
                                      url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='white'%3E%3Cpath d='M10 2h4a2 2 0 0 1 2 2v2h4a2 2 0 0 1 2 2v3H2V8a2 2 0 0 1 2-2h4V4a2 2 0 0 1 2-2zm4 4V4h-4v2h4zM2 13h20v5a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-5z'/%3E%3C/svg%3E")
                                        center / 18px 18px no-repeat,
                                      linear-gradient(45deg, #3b82f6, #14b8a6);

                                    /* subtle depth (your preferred look) */
                                    box-shadow:
                                      0 0 0 8px rgba(59,130,246,0.20),
                                      0 0 10px rgba(20,184,166,0.35); 
                                  }
              /* --- Item content --- */
              .t-date{
                        font-size: 1rem;
                        opacity: 1.85;
                        margin-bottom: 6px;
                        font-weight: 600;
                      }

              .t-role{
                        font-size: 1.3rem;
                        font-weight: 800;
                        margin: 0 0 4px 0;
                        color: #7fffe1;/*55B4A8*/
                      }

              .t-org{
                      font-size: 1.1rem;
                      font-weight: 700;
                      margin: 0 0 8px 0;
                      color: #4F83EB;
                    }

              .t-desc{
                        font-size: 0.95rem;
                        line-height: 1.45;
                        color: #fcfcfc;
                        margin: 0;
                        text-align: justify;
                      }
                      
              .highlight-key{
                              font-style: italic;
                              text-decoration: underline;
                              text-underline-offset: 3px;
                            }
                            
              .t-tags{
                        margin-top: 10px;
                        display: flex;
                        flex-wrap: wrap;
                        gap: 8px;
                      }

              .t-tag{
                      font-size: 0.9rem;
                      padding: 4px 10px;
                      border-radius: 999px;
                      border: 1px solid rgba(255,255,255,0.18);
                      background: linear-gradient(45deg, #3b82f6, #14b8a6);
                      color: #fcfcfc;
                      font-weight: 500;
                    }
              .t-link{
                        color: #7FFFE1;                 /* bright, readable */
                        text-decoration: underline;
                        text-underline-offset: 3px;
                        font-weight: 600;
                      }

              .t-link:hover{
                              color: #f5c542;
                            }

              /* Make sure the two columns don't look cramped on smaller widths */
              @media (max-width: 900px){
                                        .timeline-title{ text-align: center; }
                                      }
              /* GPA pill */
              .gpa-pill{
                          display: inline-block;
                          padding: 4px 12px;
                          margin-top: 8px;
                          margin-bottom: 8px;
                          margin-right: 8px;
                          font-size: 1rem;
                          font-weight: 600;

                          color: #fcfcfc;
                          background: transparent;

                          border: 1px solid rgba(255,255,255,1);
                          border-radius: 999px;
                        }
                                                                                                              
              /* Social icon buttons */
              .social-buttons{
                                display: flex;
                                justify-content: center;
                                gap: 18px;
                                margin-top: 2px;
                              }

              .social-btn{
                          width: 46px;
                          height: 46px;
                          border-radius: 50%;
                          display: flex;
                          align-items: center;
                          justify-content: center;
                          text-decoration: none;
                          background: #5A5A5A;                 /* WHITE background */
                          border: 1px solid rgba(0,0,0,0.15); 
                        }

              .social-btn:hover{
                                  transform: translateY(-2px);
                                  background: #f5c542;
                                  box-shadow: 0 6px 18px rgba(0,0,0,0.4);
                                }

              /* Icon sizing */
              .social-btn img{
                                width: 30px;
                                height: 30px;
                              /* grey tone */
                                filter: brightness(0);                              }

    /* ---------- MOBILE RESPONSIVE OVERRIDES ---------- */
    @media (max-width: 768px){

                              /* Reduce global padding and avoid horizontal scroll */
                              html, body { overflow-x: hidden; }
                              .block-container { padding-top: 4.2rem !important; padding-left: 1rem !important; padding-right: 1rem !important; }
                        
                              /* Nav: stack, reduce margins, allow wrap */
                              .top-nav-wrap{
                                                padding: 8px 10px !important;
                                                flex-wrap: wrap !important;
                                                gap: 8px !important;
                                              }
                              .top-nav-brand{
                                                width: 100% !important;
                                                margin-left: 0 !important;
                                                justify-content: center !important;
                                                align-items: center !important;
                                              }
                              .top-nav-links{
                                                width: 100% !important;
                                                margin-right: 0 !important;
                                                justify-content: center !important;
                                                flex-wrap: wrap !important;
                                                gap: 12px !important;
                                                font-size: 0.95rem !important;
                                              }
                        
                              /* HERO: scale down huge typography */
                              #home h1 { font-size: 2.4rem !important; line-height: 1.1 !important; }
                              #home h3 { font-size: 1.3rem !important; }
                              #home h4 { font-size: 1.0rem !important; line-height: 1.4 !important; padding: 0 8px !important; }

                              /* CTA buttons: full width on mobile */
                              .cta-button{
                                            display: block !important;
                                            width: 100% !important;
                                            max-width: 420px !important;
                                            margin: 12px auto 0 auto !important;
                                            text-align: center !important;
                                            padding: 12px 18px !important;
                                            font-size: 1rem !important;
                                          }
                        
                              /* Timeline: tighten spacing */
                              .timeline{ padding-left: 18px !important; }
                              .timeline:before{ left: 6px !important; }
                              .t-item{ margin-left: 6px !important; padding: 12px !important; }
                              .t-item.academic:before, .t-item.work:before{
                                                                            left: -32px !important;
                                                                            width: 22px !important;
                                                                            height: 22px !important;
                                                                            top: 14px !important;
                                                                            background-size: 16px 16px, auto !important;
                                                                          }
                              .t-role{ font-size: 1.1rem !important; }
                              .t-org{ font-size: 1.0rem !important; }
                              .t-desc{ font-size: 0.95rem !important; text-align: left !important; }
                        
                              /* Pills/tags wrap nicely */
                              .t-tags{ gap: 6px !important; }
                              .t-tag{ font-size: 0.85rem !important; padding: 3px 9px !important; }
                        
                              /* Social buttons: smaller */
                              .social-btn{ width: 42px !important; height: 42px !important; }
                              .social-btn img{ width: 26px !important; height: 26px !important; }
                            }
                            
              .circle-image {
                            width: 400px;
                            height: 400px;
                            border-radius: 50%;
                            overflow: hidden;
                            box-shadow: 0 0 50px #f5c542;
                            border: 1px solid #f5c542;
                            transform: translateY(50px);
                            margin: auto;
                        }
              
              .circle-image img {
                                    width: 100%;
                                    height: 100%;
                                    object-fit: cover;
                                }


            /* ===== MOBILE-ONLY OVERRIDE FOR CIRCLE IMAGE ===== */
            /* This block ONLY activates when viewport is 768px or narrower */
              @media only screen and (max-width: 768px) {
                .circle-image {
                                width: 240px !important;
                                height: 240px !important;
                                transform: translateY(0px) !important;
                                margin: 10px auto 30px auto !important;
                                box-shadow: 0 0 25px #f5c542 !important;
                            }
            }
                                
            </style>""",
            unsafe_allow_html=True #<a href="#academic-journey">Academic Journey</a>
          )


st.markdown(
            """            
            <div class="top-nav-wrap">
              <div class="top-nav-brand">
                <h2 href="#brand"><span class="highlight-name">RAM.</span></h2>
              </div>
            <div class="top-nav-links">
                <a href="#home">Home</a>
                <a href="#about">About</a>
                <a href="#research">Research</a>
                <a href="#journey">Journey</a>
                <a href="#projects">Projects</a>
                <a href="#skills">Skills</a>
                <a href="#contact">Contact</a>
              </div>
            </div>
            """, unsafe_allow_html=True)

                # <a href="#thesis">Thesis Idea</a>
# <a href="#home">Home</a>
# -----------------------------
# HOME
# -----------------------------
st.markdown(
              """            
              <div id="home" style="text-align:center; padding: 60px 0 100px 0;">
                  <h1 style="font-size:6rem; margin-bottom:4px;">
                      Sundar Ram Subramanian
                  </h1>
                  <h2 style="font-weight:600; color:#fcfcfc; font-size:2.5rem;">
                      <span class="highlight-name">Graduate Researcher</span> 
                  </h2>
                  <h4 style="font-weight:600; color:#f5c542; font-size:2rem;">
                      in AI for Music and Cultural Musicology
                  </h4>
                  <h4 style="font-size: 2rem; font-weight: 300;">
                      <span class="highlight-name">
                          with focus in Music Information Retrieval, Representation learning, and Parameter-efficient adaptation of Foundational Music models
                      </span>
                      <br>
                      <span style="color:#f5c542;">
                          for culturally underrepresented musical traditions.
                      </span>
                  </h4>
              </div>
              """,
              unsafe_allow_html=True,
          )
#                       <span class="highlight-name">Data Scientist</span><span class="highlight-name"> & </span><span class="highlight-name">Machine Learning Engineer</span>
#                       Leveraging Deep Learning and Information Retrieval techniques 

st.markdown(
              """         
              <div style="text-align:center; padding-bottom: 20px;">
                  <!-- Call-to-action buttons -->
                  <div style="margin-top: 30px;">
                      <a href="#research" class="cta-button">View My Research</a>
                      <a href="https://drive.google.com/file/d/1kfo_IXKnEbAmNELHTFTagxLBcfo1gNkI/view?usp=share_link" target="_blank" rel="noopener noreferrer" class="cta-button-resume">Academic CV</a>
                  </div>
              </div>
              """,
              unsafe_allow_html=True,
          )
                      # <a href="#thesis" class="cta-button">Preliminary Thesis Idea</a>

st.write("")
st.write("")
st.write("")
st.write("")

# -----------------------------
# ABOUT
# -----------------------------
st.markdown(
            """            
            <div id="about" style="text-align:center; padding: 60px 0 40px 0; scroll-margin-top: 90px;">
            <h2>About me</h2>
            </div>
            """,
            unsafe_allow_html=True,
         )

# Two side-by-side containers
col1, col2 = st.columns([1.5, 2.5], vertical_alignment="top")

with col1:
  img_path = BASE_DIR / "images" / "profilepicture.jpg"
  # st.image(img_path, width="content")
  
  with open(img_path, "rb") as f:
      data = base64.b64encode(f.read()).decode()

  st.markdown(f"""
      <div class="circle-image">
          <img src="data:image/jpg;base64,{data}">
      </div>
  """, unsafe_allow_html=True)
    
with col2:
  st.markdown(
              """
              <div style="font-size: 1.1rem; line-height: 1.4; text-align: justify;">
                  <p>
                  I am a <span style="color: #f5c542; font-weight: 500;">Master's graduate in Information Science with a specialization in Machine Learning</span> from the University of Arizona. My primary research interests span <span class="highlight-name" style="font-weight: 500;">Deep Learning, Transfer Learning, Representation learning  and computational musicology </span>with a particular focus on <span class="highlight-name" style="font-weight: 500;">how AI systems can faithfully model culturally specific musical traditions</span> that remain underrepresented in mainstream audio corpora.
                  </p>
                  <p>
                  Recently, my Master's capstone research (mentored by Dr. Xiao Hu), focussed on leveraging <span class="highlight-name" style="font-weight: 500;">Transfer Learning</span> by adapting Meta's <span class="highlight-name" style="font-weight: 500;">MusicGen-Small foundation model</span> to Carnatic audio-to-audio continuation. Using <span class="highlight-name" style="font-weight: 500;">LoRA on EnCodec RVQ tokens</span> (~0.5% trainable parameters) over ~95.6 hours of cleaned Carnatic audio from the same CompMusic corpus, I built a hybrid evaluation framework combining training-time cross-entropy / perplexity, four boundary-continuation cosine distances (Mel / MFCC / Chroma / Onset), and a <span class="highlight-name" style="font-weight: 500;">32-participant Streamlit listening study</span> (15 Carnatic-familiar) analysed with one-sided <span class="highlight-name" style="font-weight: 500;">Holm-corrected binomial tests</span>. Listeners preferred the fine-tuned continuations on perceptual axes that included Musicality 63.0%, Continuity 62.5%, and Carnatic Authenticity 64.6% (Holm p << 0.05); with the effect concentrated among Carnatic-familiar listeners (72.2% on Authenticity) and especially on violin recordings (78&ndash;82%), consistent with a culturally specific representational shift rather than a generic acoustic gain.
                  </p>
                  <p>
                  Preceding this work,in an Information Retrieval project, I designed an end-to-end MIR pipeline that performs <span class="highlight-name" style="font-weight: 500;">tonic (Sruti) detection and standardization</span>, extracts characteristic raga features (pitch contour, interval sequences, gamaka extent / rate / modulation index, MFCC, Mel-spectrogram and chroma), and trains a <span class="highlight-name" style="font-weight: 500;">CNN + Bi-LSTM fusion model</span> for analyzing Raga embeddings and classification across eight Melakarta ragas drawn from the <span class="highlight-name" style="font-weight: 500;">Indian Art Music Raga Recognition Dataset</span> (Serr&agrave;, Ganguli, Sent&uuml;rk, Serra &amp; Gulati, 2016 - <span class="highlight-name" style="font-weight: 500;">CompMusic / MTG&ndash;UPF</span>). The system yields learned raga-conditional audio embeddings whose t-SNE structure directly diagnoses the model's per-class behaviour (test accuracy 64.6%; per-class F1 from 0.89 down to 0.00). The dominant failure mode is embedding overlap: ragas that share large portions of their swara set and differ only in subtle phrasing or gamaka contour like Kalyani and Shankarabharanam. Such pairs map to overlapping regions of the learned latent space, and the downstream classifier cannot recover a separating decision boundary. The representational limit, not the architecture, sets the per-class accuracy ceiling.This points toward  <span class="highlight-name" style="font-weight: 500;">contrastive and self-supervised pre-training</span> of raga, tala and gamaka conditional audio embeddings as the next step.
                  </p>
                  <p>
                  Prior to graduate school, I spent six years at <span class="highlight-name" style="font-weight: 500;">Titan Company Limited</span>, where I led applied deep-learning and LLM pipelines for new product development, manufacturing, merchandising and consumer analytics. That industry tenure grounds my work in <span class="highlight-name" style="font-weight: 500;">Market research, reproducible pipelines, careful evaluation, and end-to-end systems thinking</span>. I now bring the same engineering discipline to MIR research to contribute positively in the space.
                  </p>
              </div>
              """,
                  unsafe_allow_html=True
              )

st.write("")
st.write("")
st.write("")
st.write("")


# -----------------------------
# RESEARCH STATEMENT
# -----------------------------
st.markdown(
            """
            <div id="research" style="text-align:center; padding: 60px 0 20px 0; scroll-margin-top: 90px;">
              <h2>Research Interests</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
            """
            <div style="max-width: 1100px; margin: 0 auto; padding: 0 60px;">
              <div style="font-size: 1.1rem; line-height: 1.5; text-align: justify;">
                <p>
                  I am most excited by two interlinked questions. <span class="highlight-name" style="font-weight: 500;">First, how should we train deep audio models like codecs, embedding networks, and foundation music models to learn general-purpose representations that capture the structural identity of a musical tradition</span>, including the swara grammar, gamaka ornamentation, and microtonal pitch trajectories of traditional music, rather than only the surface acoustics that current Western-trained pipelines privilege?
                  <span class="highlight-name" style="font-weight: 500;">Second, how can such representations be used to fingerprint, retrieve, and adapt music at scale</span> that includes identifying a raga or composition from a short unseen recording, retrieving stylistically similar performances across artists and instruments, and steering foundation generative models toward faithful continuations of underrepresented traditions?
                </p>
                <p>
                  My existing work approaches these questions from both ends. The <span class="highlight-name" style="font-weight: 500;">Raga Identification</span> pipeline produces raga-conditional audio embeddings from a CNN + Bi-LSTM fusion over hand-engineered features, providing an interpretable latent space whose geometry directly diagnoses cultural confusions (overlapping janya scales, gamaka-light vs. gamaka-heavy ragas, and class-imbalance failure modes). The <span class="highlight-name" style="font-weight: 500;">MusicGen LoRA finetune</span> adapts a Western-pretrained foundation model toward Carnatic style with only ~0.5% of parameters trainable, and surfaces the methodological limits of generic tokenizers (EnCodec) and Western-biased evaluation metrics (fixed-window cosine distances) when applied to non-Western audio.
                </p>
                <p>
                  Looking forward, I want to extend this arc along several connected fronts. The first is pushing beyond task-specific features toward <span class="highlight-name" style="font-weight: 500;">reusable, general-purpose representations of sound and music</span> by re-training EnCodec / DAC residual codebooks on culturally specific audio so microtonal gamakas survive quantization, and exploring contrastive and self-supervised objectives over large community-driven sound corpora and Essentia-extracted feature collections. The same representation-learning toolkit naturally extends to broader sound understanding aiding robust sound-event classification, weakly-supervised tagging, and retrieval over Freesound-scale archives.
                </p>
                <p>
                  Open methodological directions I want to pursue include: <span class="highlight-name" style="font-weight: 500;">domain-aware tokenization</span> (fine-tuning EnCodec's residual codebooks on cultural audio so that gamakas survive quantization); <span class="highlight-name" style="font-weight: 500;">self-supervised and contrastive representation learning</span> tailored to microtonal pitch grammars; <span class="highlight-name" style="font-weight: 500;">audio fingerprinting</span> over learned embeddings for raga / composition / artist identification on noisy, real-world recordings; and <span class="highlight-name" style="font-weight: 500;">culture-aware evaluation methodology</span> that goes beyond fixed-window cosine distances; pitch-class-distribution similarity in cents, gamaka-aware metrics, raga-conditional embedding distances, and rigorously controlled listener studies with multiple-comparison correction.
                </p>
                <p>
                  Broadly, I see MIR as a place where cultural musicology and modern deep learning meet productively.
                </p>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")
st.write("")
st.write("")


# # -----------------------------
# # PRELIMINARY THESIS IDEA / WHY MTG-UPF
# # -----------------------------
# st.markdown(
#             """
#             <div id="thesis" style="text-align:center; padding: 60px 0 20px 0; scroll-margin-top: 90px;">
#               <h2>Preliminary Thesis Idea &middot; Why MTG&ndash;UPF</h2>
#               <span style="alignment: center; font-size: 1.1rem; color: #b3b5b4;">
#                 A draft thesis direction aligned with MTG&rsquo;s open PhD call, positioned at the intersection of representation learning and computational musicology.
#               </span>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

# st.markdown(
#             """
#             <div style="max-width: 1100px; margin: 0 auto; padding: 0 60px;">
#               <div style="font-size: 1.1rem; line-height: 1.55; text-align: justify;">
#                 <p>
#                   <span class="highlight-name" style="font-weight: 600;">Working title:</span>
#                   <em>Culture-Aware Audio Representations and Foundation-Model Adaptation for Underrepresented Musical Traditions &mdash; with Carnatic Music as a Testbed.</em>
#                 </p>
#                 <p>
#                   <span class="highlight-name" style="font-weight: 600;">Core hypothesis.</span> Modern foundation music models (MusicGen, AudioLM, MERT, CLAP) inherit a strong Western bias from their codecs, tokenizers and training corpora. Microtonal and ornamentation-rich traditions such as Carnatic, Hindustani, Arab-Andalusi, and Turkish Makam are systematically smoothed, mis-quantized, or under-discriminated by these stacks. A culture-aware reformulation &mdash; touching both representation (codecs, embeddings) and evaluation (metrics, listener studies) &mdash; can substantially improve recognition, retrieval, and generation for these traditions <em>without</em> sacrificing performance on Western audio.
#                 </p>
#                 <p>
#                   <span class="highlight-name" style="font-weight: 600;">Concrete work-streams.</span>
#                 </p>
#                 <ul style="font-size: 1.05rem; line-height: 1.6;">
#                   <li><span class="highlight-name" style="font-weight: 500;">WP1 &mdash; Domain-aware neural audio codecs (links to Bogdanov).</span> Re-train EnCodec / DAC residual-vector-quantization codebooks on Carnatic, Hindustani and other CompMusic corpora; measure reconstruction quality on gamaka-rich segments using pitch-trajectory error in cents (not generic SI-SDR), and downstream impact on MusicGen-style continuation.</li>
#                   <li><span class="highlight-name" style="font-weight: 500;">WP2 &mdash; Culture-conditioned representation learning (links to Bogdanov &amp; Serra).</span> Contrastive / self-supervised pre-training of audio embeddings that are explicitly raga-, tala- and instrument-conditional; evaluate on raga ID, artist ID, composition fingerprinting, and cross-recording similarity using Saraga and Dunya, and benchmark against Essentia&rsquo;s tonal descriptors.</li>
#                   <li><span class="highlight-name" style="font-weight: 500;">WP3 &mdash; Carnatic-aware evaluation metrics (links to Serra).</span> Replace FAD-style metrics with culture-specific objective measures &mdash; pitch-class distribution similarity in cents, gamaka extent / rate / modulation-index distributions, raga-conditional embedding distances &mdash; and design large-scale, statistically rigorous listening protocols (multi-listener, multi-tradition, multiple-comparison-corrected).</li>
#                   <li><span class="highlight-name" style="font-weight: 500;">WP4 &mdash; Open-source integration (links to Font &amp; the MTG mission).</span> Contribute the codecs, embeddings, datasets and metrics back to <em>Essentia</em>, <em>Freesound</em> and the <em>Dunya</em> ecosystem so the community can reuse them; explore Freesound-based machine-listening transfer to general-sound applications.</li>
#                 </ul>
#                 <p>
#                   <span class="highlight-name" style="font-weight: 600;">Why MTG&ndash;UPF?</span> The Music Technology Group is, to my knowledge, the only research environment in the world that brings together (a) world-leading expertise in audio representation learning and music-generative AI, (b) <em>two decades</em> of computational-musicology work on non-Western traditions through CompMusic, and (c) a deeply embedded commitment to open datasets, open code, and reproducible research through Essentia, Freesound and Dunya. My existing work already builds on MTG-released artefacts &mdash; the CompMusic Indian Art Music corpus underpins both my Raga ID and my MusicGen LoRA capstone &mdash; and a PhD at MTG would let me deepen that collaboration, contribute back to the open ecosystem, and pursue the culturally-grounded research agenda above under the supervision of researchers who pioneered the field.
#                 </p>
#                 <p>
#                   <span class="highlight-name" style="font-weight: 600;">Fit with the candidate profile.</span> M.S. in Information Science (Machine Learning, GPA 4.0/4.0) from the University of Arizona; six years of production ML engineering at Titan Company; strong Python (PyTorch, Hugging Face, AudioCraft, librosa); audio signal processing experience through both capstones; lifelong listener of Carnatic music; comfortable in interdisciplinary, multicultural research environments.
#                 </p>
#               </div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

# st.write("")
# st.write("")
# st.write("")


# -----------------------------
# JOURNEY
# -----------------------------
st.markdown(
              """
              <div id="journey" style="text-align:center; padding: 60px 0 20px 0; scroll-margin-top: 90px;">
              <h2>Journey</h2>
              </div>
              """,
              unsafe_allow_html=True,
          )

# -----------------------------
# ACADEMIC JOURNEY (MOVED UP)
# -----------------------------
st.markdown(
              """
              <div style="text-align:center; padding: 10px 0 20px 0;">
                <h3 style="font-size: 1.8rem; font-weight: 600;">Academic</h3>
              </div>
              """,
              unsafe_allow_html=True,
          )

st.markdown(
    """
    <div class="timeline">

      <div class="t-item academic">
        <div class="t-date">Jun 2024 - May 2026</div>
        <div class="t-role">M.S. in Information Science (Machine Learning)</div>
        <div class="t-org">University of Arizona</div>
        <p class="t-desc">
          <span class="highlight-key">Focus Area:</span> Music Information Retrieval, Representation Learning for Audio, Parameter-Efficient Fine-Tuning of Foundation Models (LoRA / Adapters), Deep Learning Pipelines, NLP (SemEval tasks), Computer Vision, and Agentic AI systems.
        </p>
        <div>
        <span class="gpa-pill">GPA: 4/4</span>
        <a href="https://eportfolio-sundar-ram-subramanian-masters-infosci-uofa.streamlit.app" target="_blank" class="t-link">↗︎ Academic e-Portfolio</a>
        </div>
      </div>

      <div class="t-item academic">
        <div class="t-date">Sep 2023 - Aug 2024</div>
        <div class="t-role">Post Graduate Certification in Business Management</div>
        <div class="t-org">Xavier&rsquo;s School of Management (XLRI)</div>
        <p class="t-desc">
          <span class="highlight-key">Focus Area:</span> Business Management, International Business Development, Economics &amp; Finance.
        </p>
        <div>
        <span class="gpa-pill">GPA: 6.52/8</span>
        </div>
      </div>

      <div class="t-item academic">
        <div class="t-date">Dec 2021 - Jan 2023</div>
        <div class="t-role">Post Graduate Program in Data Science and Business Analytics</div>
        <div class="t-org">University of Texas at Austin</div>
        <p class="t-desc">
          <span class="highlight-key">Focus Area:</span> Advanced Statistical Modelling, EDA, Supervised &amp; Unsupervised Learning, Time Series Forecasting, SQL, Tableau &amp; Dashboarding.
        </p>
        <div>
        <span class="gpa-pill">GPA: 3.6/4</span>
        <a href="https://eportfolio.mygreatlearning.com/sundar-ram-s" target="_blank" class="t-link">↗︎ Academic e-Portfolio</a>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)
        # <p>&nbsp;</p>
        # <div class="t-date">Key Projects:</div>
        # <p class="t-desc">
        #   <span class="highlight-key">Capstone Research (INFO 698) </span>on Fine-Tuning Foundational Music Model for Carnatic Audio Continuation. Mentored by Dr. Xiao Hu, this independent research study is a LoRA adaptation of Meta's MusicGen-Small over EnCodec RVQ tokens, evaluated with cross-entropy / perplexity, boundary-continuation cosine distances, and a Holm-corrected human listening study.
        # </p>
        # <p class="t-desc">
        #   <span class="highlight-key">IR Project (INFO 556):</span> Carnatic Music Raga Identification using MIR + Deep Learning. End-to-end pipeline for shruti standardization, raga feature extraction, and CNN + Bi-LSTM fusion classification over 8 Melakarta ragas.
        # </p>

st.write("")

# -----------------------------
# INDUSTRY & RESEARCH JOURNEY
# -----------------------------
st.markdown(
              """
              <div style="text-align:center; padding: 30px 0 20px 0;">
                <h3 style="font-size: 1.8rem; font-weight: 600;">Research & Industrial Journey</h3>
              </div>
              """,
              unsafe_allow_html=True,
          )

st.markdown(
    """
    <div class="timeline">

      <div class="t-item work">
        <div class="t-date">Aug 2025 - Present</div>
        <div class="t-role">Graduate Researcher - Music Information Retrieval &amp; Deep Learning</div>
        <div class="t-org">The University of Arizona</div>
        <p class="t-desc">
          <span class="highlight-key">Primary MIR research (Capstone, INFO 698, mentored by Dr. Xiao Hu).</span> Fine-tuned Meta&rsquo;s MusicGen-Small foundation music model on ~95.6h of Carnatic audio (CompMusic / MTG&ndash;UPF corpus) using LoRA over EnCodec RVQ tokens (~0.5% trainable params). Hybrid evaluation: cross-entropy / perplexity, four boundary-continuation cosine distances (Mel / MFCC / Chroma / Onset), and a 32-participant Streamlit listening study (15 Carnatic-familiar) with one-sided Holm-corrected binomial tests. Headline result: significant listener preference for the fine-tuned model on all three perceptual axes; strongest effect on Carnatic Authenticity (Holm p &asymp; 9.6e-5).
          </p>
        <p>&nbsp;</p>
        <p class="t-desc">
          <span class="highlight-key">MIR + Deep Learning (IR Project, INFO 556).</span> Designed an end-to-end MIR + CNN + Bi-LSTM fusion pipeline for Carnatic raga identification across 8 Melakarta ragas using the Serrà et al. 2016 CompMusic dataset; produced 384-dim raga-conditional audio embeddings whose t-SNE geometry diagnoses embedding overlap between ragas with shared swara sets as the dominant failure mode.
          </p>
        <p>&nbsp;</p>
        <p class="t-desc">
          <span class="highlight-key">Cross-domain deep learning - NLP & CV.</span> SemEval shared tasks (STS, OffensEval, MeasEval, ComVe) using GloVe embeddings and fine-tuning of BERT / RoBERTa; a custom Computer Vision pipeline for surgical suture analysis using Roboflow annotation / augmentation and YOLO object detection.
          </p>
        <p>&nbsp;</p>
        <p class="t-desc">
          <span class="highlight-key">Systems & engineering.</span> A Multi-Agent Decision Support System (planning, tool use, reflection, evals) for jewellery merchandising research, and AWS-based cloud infrastructure with CI/CD pipelines for a full-stack student degree-planner web application.
          </p>
        <div class="t-tags">
          <span class="t-tag">Deep Learning</span>
          <span class="t-tag">Transfer Learning</span>
          <span class="t-tag">Fine Tuning LLMs/ MLLMs</span>
          <span class="t-tag">Parameter-Efficient Fine-Tuning</span>
          <span class="t-tag">Representation Learning</span>
          <span class="t-tag">Audio Representation Learning</span>
          <span class="t-tag">Audio Embeddings</span>
          <span class="t-tag">Agentic AI</span>
          <span class="t-tag">Agentic Reflection</span>
          <span class="t-tag">Agentic Tool Use</span>
          <span class="t-tag">Agentic Evals</span>
          <span class="t-tag">Multi Agentic Workflow</span>          
          <span class="t-tag">Semantic Textual Similarity</span>
          <span class="t-tag">AWS CodePipeline</span>          
          <span class="t-tag">AWS CodeBuild</span>          
          <span class="t-tag">AWS Amplify</span>          
          <span class="t-tag">AWS Lambda</span>          
          <span class="t-tag">AWS S3</span>
          <span class="t-tag">AWS DynamoDB</span>
          <span class="t-tag">AWS ECR</span>
          <span class="t-tag">AWS ECS</span>
          <span class="t-tag">Docker</span>
          <span class="t-tag">Containerization</span>          
          <span class="t-tag">Digital Signal Processing</span>
          <span class="t-tag">Computer Vision</span>          
          <span class="t-tag">Image Annotation</span>          
          <span class="t-tag">Object Detection</span>          
        </div>
      </div>

      <div class="t-item work">
        <div class="t-date">Oct 2023 - Jul 2025</div>
        <div class="t-role">Assistant Manager - Data Science &amp; Advanced Analytics</div>
        <div class="t-org">Titan Company Limited</div>
        <p class="t-desc">
          Led the Data Centre of Excellence, designing and deploying production-grade GenAI / ML / fine-tuning pipelines in Python &amp; SQL. The work below demonstrates end-to-end deep-learning systems, careful evaluation, and reproducible pipelines.
        </p>
        <p class="t-desc">&nbsp;</p>
        <p class="t-desc">
          <span class="highlight-key">Multilingual customer segmentation (Deep Learning):</span> Built a deep-learning language-classification pipeline that segments customers by mother-tongue from short text fields; integrated into the ETL via AWS Glue for online inference on new records.
        </p>
        <p class="t-desc">&nbsp;</p>
        <p class="t-desc">
          <span class="highlight-key">LLM &amp; multimodal pipelines (Generative AI):</span> Three production GenAI systems that includes LLM-driven sentiment analytics on Google review text; an LLM + audio feedback pipeline for merchandise insights from non-purchasers; and an image-conditioned LLM pipeline that extracts prominent design elements from jewellery images and auto-generates structured product descriptions.
        </p>
        <p class="t-desc">&nbsp;</p>
        <p class="t-desc">
          <span class="highlight-key">Engineering practice:</span> Streamlit-deployed analytical applications, dashboards, evaluation harnesses, and Tableau geo-spatial dashboards.
        </p>
        <div class="t-tags">
          <span class="t-tag">LLM Pipelines</span>
          <span class="t-tag">Multimodal (Text + Image + Audio)</span>
          <span class="t-tag">Deep Learning</span>
          <span class="t-tag">Embedding-based Classification</span>
          <span class="t-tag">AWS Glue / S3</span>
        </div>
      </div>

      <div class="t-item work">
        <div class="t-date">Apr 2023 - Mar 2024</div>
        <div class="t-role">Young Leadership Program - Lead Data Scientist (Merchandising)</div>
        <div class="t-org">Titan Company Limited</div>
        <p class="t-desc">
          - Selected in the top 10% of high-potential young talent; fully sponsored Post-Graduate Certificate in Business Management at XLRI alongside data-science delivery.
        </p>
        <p class="t-desc">
          - Led product attribution and inventory segmentation analytics for the jewellery merchandising function; the project surfaced the data and feature gaps that later motivated my LLM-based product-annotation pipeline.
        </p>
        <div class="t-tags">
          <span class="t-tag">Product Attribution</span>
          <span class="t-tag">Inventory Analytics</span>
          <span class="t-tag">Leadership</span>
        </div>
      </div>

      <div class="t-item work">
        <div class="t-date">Jul 2019 - Mar 2023</div>
        <div class="t-role">Lead Data Scientist - New Product Development</div>
        <div class="t-org">Titan Company Limited</div>
        <p class="t-desc">
          - Owned analytics and project management for ~600 watch designs at Brand Sonata; 
        </p>
        <p class="t-desc">
          - Carried out Market Research to identify vaccum in the Brand portfolio, leading the innovation of first ever branded skeletal quartz watch and grew the &gt; INR 2,000 price-band portfolio by 170%.
        </p>
        <p class="t-desc">
          - Reduced proto-dial manufacturing lead time from 45 to 10 days (77%) via causal inferencing of manufacturing techniques. Placed 13th nationally in the Kaizen competition. 
        </p>
        <p class="t-desc">
          - Built lead-time / attribute correlation matrices that allowed certain SKUs to go to production without prototype approval.
        </p>
        <div class="t-tags">
          <span class="t-tag">Causal Inference</span>
          <span class="t-tag">Manufacturing Analytics</span>
          <span class="t-tag">Decision Support Systems</span>
          <span class="t-tag">Project Management</span>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
st.write("")
st.write("")
st.write("")

# -----------------------------
# PROJECTS
# -----------------------------
st.markdown(
              """
            <div id="projects" style="text-align:center; padding: 60px 0 20px 0; scroll-margin-top: 90px;">
              <h2>Featured Projects</h2>
            </div> 
            <div <span style="text-align:center; font-size: 1.1rem; color: #b3b5b4;">Music Information Retrieval, Representation Learning, and Parameter-Efficient adaptation of Foundation Music Models, along with cross-domain DeepLearning work.</span>
            </div>
              """,
              unsafe_allow_html=True,
          )

st.write("")
st.write("")
st.write("")
st.write("")
# ===== RESEARCH ROW (3 columns) =====
col1, col2, col3 = st.columns(3, vertical_alignment="top")

# ----- CARD 1: MusicGen LoRA Capstone -----
with col1:
    with st.container(border=True, height=720):
        st.markdown(
            f"""
            <h4 style="text-align:center;font-size: 1.5rem; font-weight: 500; margin-bottom: 0;">
              <div><span class="highlight-name">Fine-Tuning MusicGen-Small for Carnatic Audio Continuation</span></div>
            </h4>
            """,
            unsafe_allow_html=True,
        )
        img_path = BASE_DIR / "images" / "musicgen.jpg"
        st.image(img_path, use_container_width=True)
        selected_categories = ["Foundation Music Models", "LoRA / PEFT", "EnCodec RVQ Tokens", "Cultural Domain Adaptation", "Listening Study", "Holm-Corrected Significance"]
        categories = st.pills(
            "",
            selected_categories,
            selection_mode="multi",
            default=selected_categories,
            key=f"project_categories_f1"
        )
        st.markdown(
            """
            <a href="https://github.com/sundarram1608/finetuning-musicgen-small-carnatic-continuation.git" target="_blank" class="t-link">↗︎ Code Repo</a> &nbsp;&middot;&nbsp;
            <a href="https://capstone-user-evaluation-survey.streamlit.app" target="_blank" class="t-link">↗︎ Listening Study</a>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("""
            **Capstone (INFO 698)** &middot; Mentored by Dr. Xiao Hu. LoRA adaptation of Meta&rsquo;s MusicGen-Small over EnCodec RVQ tokens, trained on ~95.6h of cleaned Carnatic audio from the CompMusic / MTG&ndash;UPF Indian Art Music corpus (Serr&agrave; et al. 2016). Evaluated with cross-entropy / perplexity, four boundary-continuation cosine distances (Mel / MFCC / Chroma / Onset), and a 32-participant Streamlit listening study analysed with one-sided Holm-corrected binomial tests.

            **Headline result:** listeners preferred the fine-tuned continuations on perceptual axes of Musicality 63.0%, Carnatic Authenticity **64.6% (Holm p &asymp; 9.6e-5)**, & Continuity 62.5% with the effect concentrated among Carnatic-familiar listeners (72.2% on Authenticity, Holm p = 4.4e-5).
        """)
        # with st.expander("View research deep-dive"):
        #     st.markdown("""
        #         **Motivation.** Foundation music models such as MusicGen, AudioLM and MusicLM are pretrained on Western-dominated corpora and systematically underperform on non-Western traditions (Mehta et al., NAACL 2025). Carnatic music &mdash; with its raga grammar, microtonal *gamaka* ornamentation, and cyclic *tala* structures &mdash; is a particularly instructive stress test. Prompt-labelled Carnatic corpora are unavailable, so I focus on parameter-efficient, text-free audio-to-audio continuation.

        #         **Dataset.** *Indian Art Music Raga Recognition Dataset* (Serr&agrave;, Ganguli, Sent&uuml;rk, **Serra X.**, Gulati 2016, CompMusic / UPF, Zenodo). Saraga (Srinivasamurthy, Gulati, Repetto et al. 2021) was considered but the Serr&agrave; dataset was chosen for its structured artist/raga layout and research-only licensing. Preprocessing: MP3 &rarr; 32 kHz mono WAV; silence trim at amplitude 0.01; non-overlapping 10s clips (320,000 samples); quality filters (min RMS 0.005, max near-zero ratio 0.30, min non-silent ratio 0.60). Yields **426 source recordings &rarr; 39,162 segments &rarr; 34,400 accepted &asymp; 95.6 hours** of cleaned audio. Recording-level train / val / test split (seed 42): 361 / 22 / 43 recordings = 28,485 / 2,168 / 3,747 segments = ~79.1 / 6.0 / 10.4 hours.

        #         **Method.** Fine-tuned the LM transformer of `facebook/musicgen-small` with LoRA via the AudioCraft framework (Apple-Silicon fork, MPS backend). EnCodec RVQ tokens pre-cached to `.pt` payloads. LoRA wraps every `nn.Linear` in the LM transformer (Q/K/V/out-proj + MLP); `condition_provider` excluded (unconditional continuation). Hyperparameters: rank `r = 8` (~0.5% trainable params), `&alpha; = 16`, dropout `0.05`; AdamW, `lr = 1e-4`, weight decay `1e-4`; batch 1 with 8-step gradient accumulation (effective batch 8); gradient clipping `1.0`; 10 epochs with early-stop patience 3. Loss: token-level CE on EnCodec codes via `compute_predictions`.

        #         **Hybrid evaluation (Lerch et al. 2025 taxonomy).** *Training-side:* per-epoch train/val CE and val perplexity. *Inference-side:* 50 held-out prompts (`random_state=42`); each generates a 20s clip (10s prompt + 10s continuation) on CPU for determinism. Four boundary-cosine metrics on 1s windows: 128-bin Mel, 20-coef MFCC, 12-bin Chroma, onset envelope (3,700 valid prompt windows). *Listening study:* Streamlit app + Google Sheets logging via Drive API; **32 participants (15 Carnatic-familiar, 17 unfamiliar)**; 6 Likert trials (Musicality / Continuity / Carnatic Authenticity, 1&ndash;5) + 6 forced-choice A/B (randomized order); stratified by performer type (vocal, violin, mridangam/tabla). One-sided binomial tests (H<sub>0</sub>: p &le; 0.5), **Holm correction** across the 3 pairwise questions, &alpha; = 0.05.

        #         **Results &mdash; training.** Val CE 4.1920 &rarr; 4.1402 across all 10 epochs (monotonic, best = epoch 10); val perplexity 66.18 &rarr; 62.84; no divergence.

        #         **Results &mdash; boundary distances.** Mel 0.0062 &rarr; 0.0061 (&minus;1.3%); MFCC 0.0252 &rarr; 0.0241 (**&minus;4.2%, largest gain**); Chroma 0.1358 &rarr; 0.1363 (+0.4%, marginal regression &mdash; consistent with shared sruti across baseline and fine-tune); Onset 0.3792 &rarr; 0.3746 (&minus;1.2%). Per-clip win rate ~49&ndash;51% &mdash; 1s cosine windows are noisy per-sample estimators.

        #         **Results &mdash; listening study.** Overall MOS (n = 192): Musicality 3.58, Continuity 3.48, Authenticity 3.78. Pairwise preference: Musicality **63.0%** (Holm p = 0.000378), Authenticity **64.6%** (Holm p = 9.6e-5, strongest), Continuity **62.5%** (Holm p = 0.000378) &mdash; all three significant. *Sub-group:* Carnatic-familiar listeners &mdash; all three significant (Authenticity 72.2%, Holm p = 4.4e-5); unfamiliar listeners &mdash; none significant after correction. *By performer type:* Violin **78&ndash;82%** FT-preferred (all Holm p &lt; 1e-6); Mridangam 69&ndash;72% (directional, Holm p ~ 0.06&ndash;0.10); Vocal 48&ndash;52% (null &mdash; the pretrained baseline is already reasonable on solo voice). The combination of "significant only for familiar listeners" and "significant on instrumental tracks where Western priors are weakest" is the cleanest single piece of evidence that LoRA is producing culturally-specific representational change, not a generic acoustic gain.

        #         **Limitations the author calls out.** (i) Canonical FAD could not be computed in its standard form because the silence-trim cleaning step destroyed prompt-to-real-continuation alignment. (ii) Per-clip wins on boundary cosine distances are only ~50%, exposing 1s windows as noisy proxies. (iii) Compute restricted to MusicGen-small on a single Apple-Silicon GPU. (iv) EnCodec (Western-trained) may smooth gamaka microtones at quantization time. (v) Only 32 participants and a 10s continuation horizon; alapana &rarr; kriti &rarr; tani transitions are out of scope.

        #         **Future work.** Re-segment to preserve prompt+ground-truth-continuation pairs (restoring FAD / KL / embedding metrics); scale to MusicGen-medium/large with higher LoRA rank; fine-tune EnCodec codebooks on Carnatic audio (or full encoder-quantizer-decoder co-training); adopt Carnatic-aware objective metrics (pitch-class similarity in cents-mod-1200, gamaka extent / rate / modulation-index distributions, raga-conditional embedding distances); minute-scale continuation horizons; MusicRL-style RLHF using the listening-study preferences as the reward signal; LoRA + soft-prompt hybrids for explicit style steering.

        #         **Reproducibility.** All preprocessing, training, evaluation, and listening-study code is open-source on GitHub; the listening-study Streamlit app is live and uses the Google Drive API for response logging.
        #     """)

# ----- CARD 2: Raga Identification -----
with col2:
    with st.container(border=True, height=720):
        st.markdown(
            f"""
            <h4 style="text-align:center;font-size: 1.5rem; font-weight: 500; margin-bottom: 0;">
              <div><span class="highlight-name">MIR + Deep Learning for Carnatic Raga Identification</span></div>
            </h4>
            """,
            unsafe_allow_html=True,
        )
        img_path = BASE_DIR / "images" / "carnatic.jpg"
        st.image(img_path, use_container_width=True)
        selected_categories = ["Music Information Retrieval", "Pitch Contour & Gamakas", "CNN + Bi-LSTM Fusion", "Raga Embeddings", "t-SNE Analysis"]
        categories = st.pills(
            "",
            selected_categories,
            selection_mode="multi",
            default=selected_categories,
            key=f"project_categories_f2"
        )
        st.markdown(
            """
            <a href="https://github.com/sundarram1608/Carnatic-Music-Raga-Identification-using-MIR-and-Deep-Learning.git" target="_blank" class="t-link">↗︎ Code Repo</a>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("""
            **Information Retrieval Project (INFO 556).** End-to-end MIR pipeline for raga classification of unseen Carnatic clips: tonic (Sruti) detection &amp; standardization to C3, multi-family raga feature extraction (pitch contour, interval sequence, gamaka extent / rate / modulation index, Mel-spectrogram, MFCC, chroma), and a CNN + Bi-LSTM fusion classifier over 8 Melakarta ragas drawn from the CompMusic / MTG-UPF Indian Art Music Raga Recognition Dataset.

            **Headline result:** 64.58% test accuracy, test loss 1.04; learned 384-dim raga embeddings reveal interpretable cluster structure in t-SNE that directly diagnoses per-class success / failure as a function of Raga overlap.
        """)
        # with st.expander("View research deep-dive"):
        #     st.markdown("""
        #         **Motivation.** Indian Art Music is fundamentally melodic and microtonal; raga identification is a core MIR task that is foundational to retrieval, recommendation, and culturally aware AI tooling (Koduri & Gulati 2011 survey; Kreiman & Narayanan 2024). Boghdady & Ewalds-Kvist (2020) show that music genre affects cognitive task performance, motivating downstream therapy / focus applications.

        #         **Dataset.** *Indian Art Music Raga Recognition Dataset* (Serr&agrave;, Ganguli, &Scedil;ent&uuml;rk, **Serra X.**, Gulati 2016, CompMusic / UPF, Zenodo DOI 10.5281/zenodo.7278511). Four candidate Kaggle datasets explicitly rejected (no audio, complex directory structure, or YouTube-dependence). **8 Melakarta ragas** chosen to avoid janya-raga grammar complexity: Hanumathodi, Harikambhoji, Kaamavardhini, Kalyani, Kharaharapriya, Mayamalavagowla, Shankarabharanam, Shanmugapriya. *Class counts are imbalanced:* 194 / 102 / 125 / 69 / 195 / 93 / 130 / 49 respectively &mdash; Kalyani and Shanmugapriya are under-supported, which directly drives the per-class failures observed downstream.

        #         **Pipeline.** Three modular stages: (1) **Sruti extraction &amp; standardization** &mdash; STFT-based pitch tracking (`librosa.piptrack`) + pitch-class histogram + peak detection identifies the artist&rsquo;s tonic in Hz &rarr; MIDI &rarr; swara; all audio is pitch-shifted to C3 (130.8128 Hz) via `librosa.effects.pitch_shift` and segmented into 30s clips. (2) **Raga feature extraction** &mdash; per-clip extraction of `librosa.pyin` f0 contour (Hz and cents-mod-1200 relative to tonic), interval sequence (delta-cents), first / second derivatives of f0, **gamaka descriptors** (Extent = local std of f0 in cents; Rate = zero-crossings of f0 derivative; Modulation Index = Extent/Rate), 128-bin Mel-spectrogram, MFCC + &Delta; + &Delta;&Delta;, and 12-bin chroma. (3) **Fusion deep learning** &mdash; a CNN branch over the Mel-spectrogram (~218M params) yields a 256-dim spectral embedding; a Bi-LSTM branch (256 units) over the (2810, 7) pitch/interval/derivatives/chroma sequence (~172K params) yields a 128-dim melodic embedding; concatenated 384-dim fusion embedding feeds a softmax classifier trained with Adam + categorical cross-entropy, stratified split, one-hot labels, early stopping, checkpointing, and LR scheduling.

        #         **EDA.** f0 distributions confirm that sruti standardization succeeds. Pitch-class profiles show that all ragas share peaks at Sa / Pa / upper-Sa due to tonic fixation, with the discriminative power lying in Ri / Ga / Ma / Dha / Ni. Median pitch contours capture each raga&rsquo;s characteristic shape (Shanmukhapriya flat plateau, Harikambhoji downward fluctuations, Mayamalavagowla heavy kampita, Shankarabharanam mid-range with dip). Raga-raga correlation matrices make the difficulty of the task visible.

        #         **Results.** Training and validation curves stabilize at 65&ndash;75% accuracy by epoch 35&ndash;40 with minimal train&ndash;val gap (no overfitting). **Held-out test accuracy: 64.58%; test loss: 1.04.** Per-class F1: **Kharaharapriya 0.89, Hanumathodi 0.74**, Kaamavardhini / Mayamalavagowla / Shankarabharanam ~0.56&ndash;0.61, **Kalyani and Shanmugapriya = 0.00** (precision and recall both zero). The t-SNE projection of the learned 256-dim fused embedding shows well-separated clusters for the high-F1 classes (Hanumathodi, Kharaharapriya) and overlapping clusters for the failures &mdash; cross-referenced with class frequency, the failures are explained by severe class imbalance (Shanmugapriya n = 49, Kalyani n = 69 vs. Kharaharapriya n = 195) and by shared swara sets with phrasing/gamaka differences not yet captured in the feature stack (Shankarabharanam vs. Kalyani in particular).

        #         **Limitations the author calls out.** Limited and imbalanced dataset (chosen due to compute/time constraints); overlapping ragas sharing swara sets but differing in phrasing/gamakas; tonic-detection errors (mitigated via `piptrack` + standardization); noisy pitch contours from gamakas (mitigated by median smoothing + feature fusion).

        #         **Future work.** Broaden and balance the corpus, especially under-sampled ragas; add user-centric expressive features (microtonal oscillations, timbre shifts, emotional intent); experiment with audio transformers / multimodal sequence models; build a real-time Shazam-like raga identifier; integrate with downstream mood-aware curation and pedagogical tools. *This project directly motivates WP2 + WP3 of my proposed PhD thesis at MTG&ndash;UPF.*
        #     """)

# ----- CARD 3: Cross-Domain Deep Learning -----
with col3:
    with st.container(border=True, height=720):
        st.markdown(
            f"""
            <h4 style="text-align:center;font-size: 1.5rem; font-weight: 500; margin-bottom: 0;">
              <div><span class="highlight-name">Cross-Domain Deep Learning: NLP, Vision &amp; Multimodal</span></div>
            </h4>
            """,
            unsafe_allow_html=True,
        )
        img_path = BASE_DIR / "images" / "nlp.jpg"
        st.image(img_path, use_container_width=True)
        selected_categories = ["Transfer Learning", "BERT / RoBERTa Fine-Tuning", "GloVe Embeddings", "Semantic Textual Similarity", "Computer Vision", "VGG16 / YOLO"]
        categories = st.pills(
            "",
            selected_categories,
            selection_mode="multi",
            default=selected_categories,
            key=f"project_categories_f3"
        )
        st.markdown(
            """
            <a href="https://github.com/sundarram1608/nlp_projects.git" target="_blank" class="t-link">↗︎ NLP Repo</a> &nbsp;&middot;&nbsp;
            <a href="https://github.com/sundarram1608/Transfer-Learning-and-Fine-Tuning---Image-Classification.git" target="_blank" class="t-link">↗︎ Vision Repo</a>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("""
            **Cross-domain representation-learning**. Spans SemEval shared tasks (STS, OffensEval, MeasEval, ComVe), Computer-Vision transfer learning with VGG16 / YOLO, and multi-agent, multimodal LLM work.
        """)
        # with st.expander("View research deep-dive"):
        #     st.markdown("""
        #         **NLP (SemEval 2019&ndash;2021).** Solved SemEval Semantic Textual Similarity (sentence-pair regression), OffensEval (offensive language classification), MeasEval (measurement-expression extraction), and ComVe (commonsense validation). Techniques: GloVe word embeddings, Word Mover&rsquo;s Distance, cosine similarity over learned representations, logistic regression baselines, RNN / CNN sequence models, and fine-tuning of BERT / RoBERTa with task-specific heads.

        #         **Computer Vision.** Transfer learning with VGG16 to classify waste products (recyclable vs. organic) &mdash; preprocessing, fine-tuning, evaluation. As a Graduate Researcher, currently building a custom CV pipeline for surgical suture analysis using Roboflow-based annotation / augmentation and YOLO for object detection.

        #         **Multi-Agent &amp; LLM systems.** Multi-Agent Decision Support System for jewellery merchandising research using agentic planning, tool use, reflection, and evaluation; Streamlit interfaces with traceability and safety constraints. Adjacent industry work at Titan included LLM-driven sentiment analytics on Google reviews, jewellery image annotation pipelines, and a customer-language classification model integrated into ETL via AWS Glue.

        #         **Why this matters for MIR research.** Audio fingerprinting and raga identification are at heart *similarity-learning* problems &mdash; closely analogous to semantic textual similarity. Domain adaptation of MusicGen is structurally the same problem as adapting a Western-pretrained text encoder to a low-resource language. Working across NLP / Vision / Audio gives me a transferable toolkit for representation learning that I can bring directly to MTG&rsquo;s problems.
        #     """)

# -----------------------------
# OTHER ENGINEERING / APPLIED ML PROJECTS
# -----------------------------

st.markdown(
              """
              <div style="text-align:center; padding: 60px 0 20px 0; scroll-margin-top: 90px;">
              <h2 style="font-size: 2.8rem;">Other Engineering & Applied ML Projects</h2>
              </div>
              """,
              unsafe_allow_html=True,
          )
              # <span style="alignment: center; font-size: 1.05rem; color: #b3b5b4;">Industry-facing engineering work that demonstrates breadth across LLM systems, transfer learning, and data infrastructure.</span>

col1, col2, col3 = st.columns(3, vertical_alignment="top")

with col1:
    with st.container(border=True, height=550):
        st.markdown(
            f"""
            <h4 style="text-align:center;font-size: 1.8rem; font-weight: 500; margin-bottom: 0;">
              <div><span class="highlight-name">Multi Agentic Merchandiser</span></div>
            </h4>
            """,
            unsafe_allow_html=True,
        )
        img_path = BASE_DIR / "images" / "agentic_ai.jpg"
        st.image(img_path, use_container_width=True)
        selected_categories = ["Multi Agentic Workflow", "Agentic Evals", "Agentic Reflection", "Agentic Tool Use", "Multi Agent Orchestration","Agentic Planning","Generative AI", "Non Purchaser Analytics"]
        categories = st.pills(
            "",
            selected_categories,
            selection_mode="multi",
            default=selected_categories,
            key=f"project_categories_agen"
        )
        st.markdown(
            """
            <a href="https://github.com/sundarram1608/Multi-Agentic_Merchandiser-NonPurchaser_Analytics.git" target="_blank" class="t-link">↗︎ Code Repo</a> - for more details.
            """,
            unsafe_allow_html=True,
        )
        st.markdown("""
            Leveraged Multi Agentic AI Workflow to build a merchandiser copilot that provide insights and recommendations from Non purchasers. 
            Built with a live streamlit interface with Agentic chat environment and recommendations with Agentic reasoning, evals, reviews, traceability, Privacy, Security and .
        """)

with col2:
    with st.container(border=True, height=550):
        st.markdown(
            f"""
            <h4 style="text-align:center;font-size: 1.8rem; font-weight: 500; margin-bottom: 0;">
              <div><span class="highlight-name">LLM Powered</span></div>
              <div><span class="highlight-name">Google Review Analytics</span></div>
            </h4>
            """,
            unsafe_allow_html=True,
        )
        img_path = BASE_DIR / "images" / "gmbsentimentanalytics.jpg"
        st.image(img_path, use_container_width=True)
        selected_categories = ["Generative AI", "Web App Development", "Data Visualization", "Dashboarding"]
        categories = st.pills(
            "",
            selected_categories,
            selection_mode="multi",
            default=selected_categories,
            key=f"project_categories_a_gmb"
        )
        st.markdown(
            """
            <a href="https://github.com/sundarram1608/Google-Review-Analytics.git" target="_blank" class="t-link">↗︎ Code Repo</a> - for more details.
            <a href="https://sentiment-analytics-g-reviews.streamlit.app/" target="_blank" class="t-link"> &nbsp;&nbsp;↗︎web application</a>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("""
            Leveraged OpenAI GPT models to translate unstructured customer reviews into actionable consumer insights. 
            Also built a Streamlit-powered UI to visualize insights.
        """)


# with col3:
#     with st.container(border=True, height=520):
#         st.markdown(
#             f"""
#             <h4 style="text-align:center;font-size: 1.5rem; font-weight: 500; margin-bottom: 0;">
#               <div><span class="highlight-name">Transfer Learning for Waste Classification</span></div>
#             </h4>
#             """,
#             unsafe_allow_html=True,
#         )
#         img_path = BASE_DIR / "images" / "wasteclassification.jpg"
#         st.image(img_path, use_container_width=True)
#         selected_categories = ["Transfer Learning", "VGG16", "Computer Vision", "Fine-Tuning"]
#         categories = st.pills(
#             "",
#             selected_categories,
#             selection_mode="multi",
#             default=selected_categories,
#             key=f"project_categories_a_waste"
#         )
#         st.markdown(
#             """
#             <a href="https://github.com/sundarram1608/Transfer-Learning-and-Fine-Tuning---Image-Classification.git" target="_blank" class="t-link">↗︎ Code Repo</a>
#             """,
#             unsafe_allow_html=True,
#         )
#         st.markdown("""
#             Fine-tuned VGG16 to classify waste products as recyclable vs. organic &mdash; end-to-end transfer-learning pipeline with image preprocessing, model adaptation, and evaluation.
#         """)

# with col1:
#     with st.container(border=True, height=520):
#         st.markdown(
#             f"""
#             <h4 style="text-align:center;font-size: 1.5rem; font-weight: 500; margin-bottom: 0;">
#               <div><span class="highlight-name">Database Development &amp; Analytics System</span></div>
#             </h4>
#             """,
#             unsafe_allow_html=True,
#         )
#         img_path = BASE_DIR / "images" / "dbms.jpg"
#         st.image(img_path, use_container_width=True)
#         selected_categories = ["MySQL", "Python-SQL Integration", "CRUD", "Streamlit", "Analytics Dashboard"]
#         categories = st.pills(
#             "",
#             selected_categories,
#             selection_mode="multi",
#             default=selected_categories,
#             key=f"project_categories_a_dbms"
#         )
#         st.markdown(
#             """
#             <a href="https://github.com/sundarram1608/database_ui_development.git" target="_blank" class="t-link">↗︎ Code Repo</a>
#             """,
#             unsafe_allow_html=True,
#         )
#         st.markdown("""
#             Full-stack data management and analytics system over a modified Northwind dataset &mdash; MySQL backend, Streamlit front-end, CRUD operations, validated ingestion, and analytical dashboards.
#         """)

# with col2:
#     with st.container(border=True, height=520):
#         st.markdown(
#             f"""
#             <h4 style="text-align:center;font-size: 1.5rem; font-weight: 500; margin-bottom: 0;">
#               <div><span class="highlight-name">German Bank Loan Default Prediction</span></div>
#             </h4>
#             """,
#             unsafe_allow_html=True,
#         )
#         img_path = BASE_DIR / "images" / "loandefault.jpg"
#         st.image(img_path, use_container_width=True)
#         selected_categories = ["Classical ML", "Tree-Based Models", "Ensembles", "Cross-Validation", "Feature Importance"]
#         categories = st.pills(
#             "",
#             selected_categories,
#             selection_mode="multi",
#             default=selected_categories,
#             key=f"project_categories_a_loan"
#         )
#         st.markdown(
#             """
#             <a href="https://github.com/sundarram1608/classification_german_bank_default_prediction.git" target="_blank" class="t-link">↗︎ Code Repo</a>
#             """,
#             unsafe_allow_html=True,
#         )
#         st.markdown("""
#             Built and tuned parametric, tree-based, and ensemble classifiers on the German Credit dataset with cross-validation and feature-importance analysis to select the best model.
#         """)

# with col3:
#     with st.container(border=True, height=520):
#         st.markdown(
#             f"""
#             <h4 style="text-align:center;font-size: 1.5rem; font-weight: 500; margin-bottom: 0;">
#               <div><span class="highlight-name">Supply Chain Regression Analytics</span></div>
#             </h4>
#             """,
#             unsafe_allow_html=True,
#         )
#         img_path = BASE_DIR / "images" / "sca.jpg"
#         st.image(img_path, use_container_width=True)
#         selected_categories = ["EDA", "Linear &amp; Ensemble Regression", "Hyperparameter Tuning", "Business Intelligence"]
#         categories = st.pills(
#             "",
#             selected_categories,
#             selection_mode="multi",
#             default=selected_categories,
#             key=f"project_categories_a_sca"
#         )
#         st.markdown(
#             """
#             <a href="https://github.com/sundarram1608/supply_chain_analytics.git" target="_blank" class="t-link">↗︎ Code Repo</a>
#             """,
#             unsafe_allow_html=True,
#         )
#         st.markdown("""
#             Linear and ensemble regression models for an instant-noodles supply chain &mdash; demand-pattern analytics, inventory optimization, and targeted-advertising recommendations.
#         """)
    
# -----------------------------
# SKILLS
# -----------------------------
st.markdown(
              """            
              <div id="skills" style="text-align:center; padding: 60px 0 60px 0; scroll-margin-top: 90px;">
              <h2>Technical Skills</h2>
              </div>
              """,
              unsafe_allow_html=True,
          )


# Skills reorganized for PhD application: MIR / Audio first, then DL/AI, then engineering.
skills_map = {"Music Information Retrieval": ["MIR Pipelines", "Audio Signal Processing", "librosa", "AudioCraft / MusicGen", "EnCodec RVQ Tokens", "LoRA / PEFT on Audio LMs", "Pitch Tracking (piptrack, pyin)", "Gamaka Descriptors", "Mel-spectrogram / MFCC / Chroma", "Listener Studies", "Boundary Cosine Metrics", "Statistical Testing", "Subjective Evaluation"],
              "Artificial Intelligence": ["Deep Learning", "Generative AI", "Foundation Music Models", "Representation Learning", "Transfer Learning", "Fine-tuning LLMs / MLLMs", "Agentic AI", "RAG", "Prompt Engineering", "NLP", "Computer Vision", "Python", "PyTorch", "TensorFlow", "Keras", "Hugging Face Transformers", "NumPy", "SciPy", "Pandas", "Evaluation & Statistical Testing"],
              "Cloud, MLOps & Reproducibility": ["AWS", "Docker", "Containerization", "CI/CD", "Streamlit Applications", "Git / GitHub", "Reproducible Research Pipelines"]}
# skills_map = {
#                 "Machine Learning, AI & Data Science": ["Agentic AI", "NLP", "RAG", "Transfer Learning", "LLM Fine-tuning", "LoRA", "Computer Vision", "Information Retrieval", "Prompt Engineering", "Business Analytics"],
#                 "Programming & Databases": ["Python", "SQL", "C++", "MySQL", "Amazon Redshift"],
#                 "ML & Data science Libraries": ["TensorFlow", "PyTorch", "Keras", "Scikit-learn", "Transformers", "gensim", "SciPy", "OpenCV", "YOLO", "Pandas", "Numpy", "Matplotlib", "Seaborn", "Boto3", "mysql", "librosa"],
#                 "Cloud, MLOps & ML App Development": ["AWS", "CI/CD pipelines", "App Deployment", "Streamlit", "Web Applications", "dashboards"],
#                 "Analytics, BI Tools & Version Control": ["Tableau", "Power BI", "Advanced Excel", "KNIME", "Git", "GitHub"],
#                 "Product & Program Management": ["Product Development", "Project Management", "Stakeholder Management", "Vendor Management"],
#             }

NUM_COLS = 3
cols = st.columns(NUM_COLS, vertical_alignment="top")

for i, (group_name, group_skills) in enumerate(skills_map.items()):
    with cols[i % NUM_COLS]:
        with st.container(border=False):
            st.markdown(
                f"""
                <h4 style="text-align:left;font-size: 1.3rem; font-weight: 500; margin-bottom: 0;">
                  <div><span class="highlight-name">{group_name}</span></div>
                </h4>
                """,
                unsafe_allow_html=True,
            )

            selected = st.pills(
                                    "",
                                    group_skills,
                                    selection_mode="multi",
                                    key=f"skills_{i}"
                                )

st.write("")
st.write("")
st.write("")
st.write("")


# -----------------------------
# CERTIFICATIONS
# -----------------------------
st.markdown(
              """            
              <div style="text-align:center; padding: 60px 0 60px 0; scroll-margin-top: 90px;">
              <h2>Certifications</h2>
              </div>
              """,
              unsafe_allow_html=True,
          )


col1, col2, col3 = st.columns(3, vertical_alignment="top")

with col1:
  with st.container(border=True, height=220, horizontal_alignment="center"):
    st.markdown(
                f"""
                <h4 style="text-align:center;font-size: 1.8rem; font-weight: 500; margin: 0 0 -1px 0;line-height: 1.2;">
                <span class="highlight-name">Agentic AI</span>
                </h4>
                """,
                unsafe_allow_html=True,
            )
    selected_categories = ["Agentic Design", "Tool Use", "Evaluate and optimize AI systems"]
    categories = st.pills(
                            "",
                            selected_categories,
                            selection_mode="multi",
                            default=selected_categories,
                            key=f"agentic_ai"
                        )
    st.markdown(
                  """
                  <div style="text-align: center;">
                      <a href="https://learn.deeplearning.ai/certificates/674d7e76-8bb5-42b8-9b0f-c0edc77db81d"
                        target="_blank"
                        class="t-link">
                          ↗︎ View Credentials
                      </a>
                  </div>
                  """,
                  unsafe_allow_html=True,
              )



# st.markdown(
    #               """
    #               <div style="text-align: center;">
    #                   <p>Non Certificate course</p>
    #               </div>
    #               """,
    #               unsafe_allow_html=True,
    #           )


with col2:
  with st.container(border=True, height=220, horizontal_alignment="center"):
    st.markdown(
                f"""
                <h4 style="text-align:center;font-size: 1.8rem; font-weight: 500; margin: 0 0 -1px 0;line-height: 1.2;">
                <span class="highlight-name">Math for Data Science & Machine Learning</span>
                </h4>
                """,
                unsafe_allow_html=True,
            )
    selected_categories = ["Linear Algebra", "Probability & Statistics", "Calculus"]
    categories = st.pills(
                            "",
                            selected_categories,
                            selection_mode="multi",
                            default=selected_categories,
                            key=f"math_ds_ml"
                        )
    st.markdown(
                  """
                  <div style="text-align: center;">
                      <a href="https://coursera.org/share/ac101ae421c2af93a17d81631182c64f"
                        target="_blank"
                        class="t-link">
                          ↗︎ View Credentials
                      </a>
                  </div>
                  """,
                  unsafe_allow_html=True,
              )



with col3:
  with st.container(border=True, height=220, horizontal_alignment="center"):
    st.markdown(
                f"""
                <h4 style="text-align:center;font-size: 1.8rem; font-weight: 500; margin: 0 0 -1px 0;line-height: 1.2;">
                <span class="highlight-name">IBM - Git and GitHub</span>
                </h4>
                """,
                unsafe_allow_html=True,
            )
    selected_categories = ["Git", "GitHub", "Version Control"]
    categories = st.pills(
                            "",
                            selected_categories,
                            selection_mode="multi",
                            default=selected_categories,
                            key=f"git_github"
                        )
    st.markdown(
                  """
                  <div style="text-align: center;">
                      <a href="https://coursera.org/share/572e263774b55ba24f15077991a149e8"
                        target="_blank"
                        class="t-link">
                          ↗︎ View Credentials
                      </a>
                  </div>
                  """,
                  unsafe_allow_html=True,
              )
    
    
with col1:
  with st.container(border=True, height=220, horizontal_alignment="center"):
    st.markdown(
                f"""
                <h4 style="text-align:center;font-size: 1.8rem; font-weight: 500; margin: 0 0 -1px 0;line-height: 1.2;">
                <span class="highlight-name">LLM & LangChain</span>
                </h4>
                """,
                unsafe_allow_html=True,
            )
    selected_categories = ["Prompt Engineering", "AI Agents", "Context Management"]
    categories = st.pills(
                            "",
                            selected_categories,
                            selection_mode="multi",
                            default=selected_categories,
                            key=f"llm_langchain"
                        )
    st.markdown(
                  """
                  <div style="text-align: center;">
                      <a href="https://coursera.org/share/d11de5683f4c12e79340fb4fe51e6afe"
                        target="_blank"
                        class="t-link">
                          ↗︎ View Credentials
                      </a>
                  </div>
                  """,
                  unsafe_allow_html=True,
              )

with col2:
  with st.container(border=True, height=220, horizontal_alignment="center"):
    st.markdown(
                f"""
                <h4 style="text-align:center;font-size: 1.8rem; font-weight: 500; margin: 0 0 -1px 0;line-height: 1.2;">
                <span class="highlight-name">Keras</span>
                </h4>
                """,
                unsafe_allow_html=True,
            )
    selected_categories = ["Transfer Learning", "Image Analytics", "Model Training & Optimization"]
    categories = st.pills(
                            "",
                            selected_categories,
                            selection_mode="multi",
                            default=selected_categories,
                            key=f"keras"
                        )
    st.markdown(
                  """
                  <div style="text-align: center;">
                      <a href="https://coursera.org/share/bb546ae9b9c37d74aa776c38caaa39eb"
                        target="_blank"
                        class="t-link">
                          ↗︎ View Credentials
                      </a>
                  </div>
                  """,
                  unsafe_allow_html=True,
              )

with col3:
  with st.container(border=True, height=220, horizontal_alignment="center"):
    st.markdown(
                f"""
                <h4 style="text-align:center;font-size: 1.8rem; font-weight: 500; margin: 0 0 -1px 0;line-height: 1.2;">
                <span class="highlight-name">Tensorflow</span>
                </h4>
                """,
                unsafe_allow_html=True,
            )
    selected_categories = ["Convolutional Neural Networks", "GAN", "Reinforcement Learning"]
    categories = st.pills(
                            "",
                            selected_categories,
                            selection_mode="multi",
                            default=selected_categories,
                            key=f"tensorflow"
                        )
    st.markdown(
                  """
                  <div style="text-align: center;">
                      <a href="https://coursera.org/share/5fb0e8d0e7a80221bd40f1deca137df2"
                        target="_blank"
                        class="t-link">
                          ↗︎ View Credentials
                      </a>
                  </div>
                  """,
                  unsafe_allow_html=True,
              )


with col2:
  with st.container(border=True, height=220, horizontal_alignment="center"):
    st.markdown(
                f"""
                <h4 style="text-align:center;font-size: 1.8rem; font-weight: 500; margin: 0 0 -1px 0;line-height: 1.2;">
                <span class="highlight-name">PyTorch</span>
                </h4>
                """,
                unsafe_allow_html=True,
            )
    selected_categories = ["Data Processing", "Applied Machine Learning", "Reinforcement Learning"]
    categories = st.pills(
                            "",
                            selected_categories,
                            selection_mode="multi",
                            default=selected_categories,
                            key=f"pytorch"
                        )
    st.markdown(
                  """
                  <div style="text-align: center;">
                      <a href="https://coursera.org/share/c6815fb841b1b901c6608310647b516f"
                        target="_blank"
                        class="t-link">
                          ↗︎ View Credentials
                      </a>
                  </div>
                  """,
                  unsafe_allow_html=True,
              )
        

# -----------------------------
# CONTACT
# -----------------------------
st.markdown(
              """            
              <div id="contact" style="text-align:center; padding: 110px 0 0 0; scroll-margin-top: 90px;">
              <h2>Get in Touch</h2>
              </div>
              """,
              unsafe_allow_html=True,
          )

st.markdown(
            """
            <div style="text-align:center; color: #f5c542; font-size:1rem;">
                Let us collaborate and create a better world together!
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
            """         
            <div style="text-align:center; padding-bottom: 20px;">
                <div style="margin-top: 0px;">
                    <a href="mailto:sundarram1997@gmail.com" class="cta-button">
                        Email
                    </a>
                    <!-- View CV -->
                    <a href="https://drive.google.com/file/d/1kfo_IXKnEbAmNELHTFTagxLBcfo1gNkI/view?usp=share_link"
                       target="_blank"
                       rel="noopener noreferrer"
                       class="cta-button-resume">
                        View CV
                    </a>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

                    # <!-- Industry Resume -->
                    # <a href="https://drive.google.com/file/d/1kfo_IXKnEbAmNELHTFTagxLBcfo1gNkI/view?usp=share_link"
                    #    target="_blank"
                    #    rel="noopener noreferrer"
                    #    class="cta-button-resume">
                    #     Industry Resume
                    # </a>

st.markdown(
            """<div class="social-buttons">
              <a class="social-btn"
                 href="https://www.linkedin.com/in/sundar-ram-subramanian"
                 target="_blank"
                 rel="noopener noreferrer"
                 aria-label="LinkedIn">
                <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/linkedin.svg" alt="LinkedIn" />
              </a>
              <a class="social-btn"
                 href="https://github.com/sundarram1608"
                 target="_blank"
                 rel="noopener noreferrer"
                 aria-label="GitHub">
                <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/github.svg" alt="GitHub" />
              </a>
              <a class="social-btn"
                 href="https://medium.com/@sundarram1997"
                 target="_blank"
                 rel="noopener noreferrer"
                 aria-label="Medium">
                <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/medium.svg" alt="Medium" />
              </a>
            </div>""",
                unsafe_allow_html=True,
            )

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.divider()

# -----------------------------
# FOOTER
# -----------------------------
# st.caption("Sundar Ram Subramanian ⊙ Built with Streamlit", width = "content", text_alignment = "center")
st.markdown(
            """
            <div style="text-align:center; opacity:0.7; font-size:1rem;">
                ⓒ May 2026 ⊙ Sundar Ram Subramanian ⊙ Built with Streamlit
            </div>
            """,
            unsafe_allow_html=True,
        )
