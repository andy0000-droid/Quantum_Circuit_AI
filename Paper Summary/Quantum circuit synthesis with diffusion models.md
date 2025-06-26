# Circuit Encoding, Model And Training Pipeline
## Circuit Encoding
### Encoding Method
첫번째 차원은 큐비트, 두번째 차원은 게이트가 위치하는 시간, 세번째 차원은 게이트의 종류를 갖고 있는 3차원 형태의 텐서로 양자 회로를 인코딩
![[Diffusion Model circuit encoding.png]]
## Diffusion Model
DiffusionModel이란 주어진 훈련 데이터셋에서 확률적 분포를 생성하는 확산 과정을 학습하는 생성형 모델
	Ref. Sohl-Dickstein, Jascha, et al. "Deep unsupervised learning using nonequilibrium thermodynamics." _International conference on machine learning_. pmlr, 2015.

Diffusion Model은 latent space로부터 guide와 condition을 설정할 수 있음이 중요함

해당 논문에서는 
	Rombach, Robin, et al. "High-resolution image synthesis with latent diffusion models." _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_. 2022.
의 파이프라인을 참고함

---

CLIP Encoder와 Unitary encoder에 대한 부분을 추가적으로 살펴봐야할 듯

---
## Training Diffusion Model
훈련셋인 인코딩된 양자 회로에 다른 레벨의 가우시안 노이즈를 추가하여 noisy한 데이터셋을 준비

noise 예측 모델은 
	Rombach, Robin, et al. "High-resolution image synthesis with latent diffusion models." _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_. 2022.
의 구조를 가져옴
해당 구조는 전형적인 U-Net, 인코더와 디코더 레이아웃과 그 사이를 건너뛰는 연결이 존재
residual convolution 레이어와 cross-attention 레이어를 결합하여 네트워크를 구성

---

	NLP를 위해 transformer 모델을 사용
	the latter implements가 의미하는 부분이 cross-attention에 대한 부분인지 추가확인 필요

---

이 논문의 use-case에서는 다음과 같은 사항을 고려함
1. 큐비트 연결의 비지역성(non-locality)
2. 모든 사이즈의 양자 회로를 데이터로 받을 수 있을 것

## Inference Diffusion Model
완전히 잡음인 텐서를 넣어주면 선택한 조건에 따라 고품질 샘플을 생성할 수 있음
# Results
본 논문에서는 모델의 성능 평가를 위해 다음 두 개의 개별적인 문제를 제시함
1. Entanglement Generation
2. Unitary Compilation

1번 문제는 다른 시나리오에 대한 방법론의 잠재력을 보여주기 위한 벤치마크의 역할
2번 문제는 양자 회로 분야의 중요한 문제이고, 방법론의 전체적인 역량을 보여줄 수 있음


# Appendix A

# Appendix B

# Appendix C

# Appendix D

# Appendix E

# Appendix F

### Glossary of terms
#### SRV (Schmidt Rank Vector)
다입자 양자 상태의 얽힘 구조를 정량적으로 표현하는 개념
##### Schmidt 분해란
두 개의 부분계 $A$와 $B$로 이루어진 순수 상태 $\ket{\psi}_{AB}$는 다음과 같이 표현할 수 있음
$$

\ket{\psi}_{AB} = \sum_{i=1}^r \lambda_i \ket{a_i}_A \ket{b_i}_B

$$

$r$은 Schmidt rank로, 얽힘의 정도를 나타냄
$r+1$이면 완전한 분리 상태
$r>1$이면 얽힌 상태

본 논문에서 SRV를 사용한 이유는 