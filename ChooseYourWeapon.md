# arXiv:2304.06035v1 [cs.OH] 31 Mar 2023

## Choose Your Weapon: Survival Strategies for Depressed AI Academics
Julian Togelius and Georgios N. Yannakakis∗
April 14, 2023

### Abstract
당신은 학술 기관에서 인공지능 연구자인가요? 현재의 인공지능 발전 속도에 대응하지 못하고 불안한 감정을 느끼시나요? 인공지능 연구의 극적 발전에 필요한 컴퓨팅 및 인적 자원에 대한 접근이 없거나 매우 제한적인 느낌을 받으시나요? 당신은 혼자가 아닙니다. 글로벌 수준에서 경쟁할 수 있는 수단과 자원을 더 이상 찾을 수 없는 인공지능 학자의 수가 증가하고 있습니다. 이는 최근에 발생한 현상이지만 급속도로 가속화되고 있으며, 민간 주체들이 최첨단 인공지능 연구에 대해 거대한 컴퓨팅 자원을 투자하고 있는 실정입니다. 본 논문에서는 학술적인 지위를 유지하면서 경쟁력을 유지하기 위해 할 수 있는 것과 대학 및 민간 부문이 상황을 개선할 수 있는 방법에 대해 간략히 논합니다. 이는 전략적인 목록이 아니며, 모든 전략에 동의하지는 않을 수 있지만, 토론의 시작점이 됩니다.

### Introduction
대학에서 인공지능 연구를 수행하는 사람으로서, DeepMind, Open AI, Google Brain 및 Meta AI와 같은 기업 인공지능 연구 센터와 얽힌 복잡한 관계를 가지게 됩니다. 대규모 신경망 모델을 훈련하여 실현되지 않았던 것들을 수행하고, 기술적 한계를 뛰어넘으며 놀라운 결과를 창출하는 논문을 볼 때, 당신은 어려운 감정을 느끼게 됩니다. 한편으로는, 정말 대단하다는 생각이 들지만, 다른 한편으로는, 우리는 어떻게 따라잡을 수 있을까요? 당신은 몇 명의 박사 과정 학생과 (행운이 따르면) 몇 명의 연구원과 함께 연구실을 이끌고 있으며, 연구를 위한 몇몇 GPUs를 보유하고 있을 뿐입니다. 이러한 유형의 연구는 간단히 수행할 수 없습니다.

명확하게 말하면, 이전에는 그랬지 않았습니다. 10년 전만 해도, 괜찮은 데스크탑 컴퓨터와 인터넷 연결이 있으면 최고의 연구자들과 경쟁할 수 있는 모든 것이 있었습니다. 혁신적인 논문들은 종종 일반적인 워크스테이션에서 모든 실험을 수행한 한 두 명의 사람들에 의해 작성되었습니다. 이것은 최근 10년간 연구 분야에 진입한 사람들과 거대한 컴퓨팅 자원의 필요성이 이미 주어진 사람들에게# OpenAI의 대규모 연구 회사들과 경쟁하는 AI 학계의 어려움

OpenAI가 같은 분야에서 연구를 진행한다는 것을 알게 되면, 작은 마을 일반 상점의 소유주가 월마트가 옆에 가게를 열면 느끼는 것과 같은 기분이 들 것입니다. 이는 모두가 기여를 인정받는 개방적이고 협력적인 연구를 추구하는 것을 원하므로 안타까운 일입니다. 그래서 귀하가 제한된 팀 규모와 한정된 컴퓨터 자원을 가진 교수라면, 대규모 연구 회사들의 치열한 경쟁에 맞서 경쟁력을 유지하기 위해 무엇을 할 수 있을까요? 이는 수년간 우리와 우리의 동료들을 괴롭혀온 문제입니다. GPT-4와 같은 모델들이 충격적으로 능력이 뛰어나며 충격적으로 폐쇄적이고 출판된 세부 정보가 없는 최근 사건들은 이 질문을 더욱 긴급하게 만들었습니다. 우리는 다양한 수준의 연구원들로부터 여러 차례 직접적으로 또는 소셜 미디어를 통해 대규모 기술 회사들의 불공정한 경쟁으로 인해 의미 있는 연구를 수행하는 전망에 대해 걱정하는 의견을 들었습니다.

우리는 이에 대해 분명하게 말하고자 합니다. 우리 둘 다 안전하게 존재합니다. 우리는 학부 교수직을 가지고 있으며, 비디오 게임 분야에서 AI의 한계를 체계적으로 넓혀왔기 때문에 빠르게 학계에서 성장했습니다. 우리는 물론 직접적으로 관련된 AI 연구를 계속하길 바라지만, 이 글은 주로 직업적인 선택을 고민하는 우리의 주니어 동료들을 위해 쓰여졌습니다. 학계에 진입할 가치가 있을까요? 아니면 대규모 기술 회사에 입사할까요? 혹은 스타트업을 시작할까요? AI 직업은 좋은 선택일까요? 아니면 배관공이 되는 것이 더 좋을까요? 당신은 기계의 일부분이 되어야 할까요, 아니면 반항적인 자세를 유지해야 할까요? (당신의 직업 생활의 첫 시작이거나 교수직을 가지고 있다면 반항적인 자세를 유지하는 것이 보통 더 쉽습니다.) 얼마나 뛰어나더라도, 경쟁력을 유지하기 위한 이 귀한 싸움은 이미 지는 것일까요? 우리는 이미 우리의 법에 복종해 누워있는 것일까요? 이 논문은 실질적인 조언과 감정적인 격려, 그리고 우리 모두가 학계에서의 위치를 개선하기 위해 토론을 시작하기 위한 것입니다.

다음은 AI 학계에서 선택의 폭이 좁아진 연# AI agent that learned to craft a diamond pickaxe in Minecraft

마인크래프트에서 다이아몬드 곡괭이를 만드는 방법을 배운 AI 에이전트는 720 개의 V100 GPU에서 9 일간의 교육이 필요합니다. 하나의 실험에 수십만 달러가 필요하며, 심지어 유럽 연구위원회 (ERC) 또는 미국 국립과학재단 (NSF)의 명성있는 보조금도 이러한 수준의 투자를 지원할 수 없습니다. 하지만 클라우드 컴퓨팅에 50,000 달러를 투자하면 게임 PC를 모아 놓는 것보다 훨씬 더 많은 계산을 할 수 있으므로 적어도 약간은 확장할 수 있습니다. 그러나 대부분의 실험은 처음 시도할 때 제대로 작동하지 않습니다. 보고된 큰 실험마다 프로토타입, 개념 증명, 디버깅, 매개 변수 조정 및 실패한 시작을 수개월 또는 몇 년간 겪게 됩니다. 이러한 수준의 컴퓨팅이 항상 사용 가능해야 합니다.

# Scale Down

문제를 우회하는 인기있는 방법 중 하나는 새로운 접근법의 이론적 이점을 증명하거나 새로운 방법의 상대적 이점을 보여주는 간단하면서 대표적인 (장난감) 문제에 초점을 맞추는 것입니다. 최근에 발표된 'Behavior Transformers' 논문에서는 간단한 다중 레이어 퍼셉트론으로 해결할 수 있는 장난감 네비게이션 작업에서 이 방법의 이점을 보여주었습니다. 유사한 방식이 [11]에서도 사용되었습니다. 그러나 이러한 연구는 대규모 모델과 중요한 컴퓨팅을 필요로하는 인기있는 게임 및 로봇 벤치마크 문제에서 알고리즘의 성능을 입증하기 때문에 영향력이 크다고 할 수 있습니다. [10]에서도 비슷한 패턴을 관찰할 수 있습니다. 장난감(도박) 환경에서 케이스를 제시하지만 알고리즘이 보다 복잡하지만 계산적으로 무거운 문제에서 상대적 이점을 보여주기 때문에 영향력이 크다고 할 수 있습니다.

# Reuse and Remaster

지난 10년간 AI가 빠르게 발전한 핵심 이유 중 하나는 연구자들이 코드와 모델을 공개적으로 공유하기 때문입니다. 모델 공유와 코드 접근성은 과거 AI 연구자들의 표준이나 우선순위가 아니었습니다. ImageNet, ViT 또는 GPT의 변형과 같은 사전 훈련된 대규모 모델에 액세스할 수 있다는 것은 시간과 노력을 절약할 수 있으며, 자신의 특정 문제에 대해 모델의 작은 부분을 미세 조정할 수 있기 때문입니다. 

# Analysis Instead of Synthesis

공개적으로 사용 가능한 사전 훈련된 모델을 분석하는 것은 새로운 기능을 직# Probing and Developing
다양한 마인드셋으로 분석을 할 수 있다. 배운 회로와 메커니즘을 찾아서 묘사하는 것은 유용하며, 우리가 이를 토대로 미래에 더 나은 모델을 만들 수 있도록 도울 수 있다. 하지만, 가독성을 높이기 위해 큰 모델을 만들려는 사람들이 말하는 것과 달리, 가플라이 역할을 할 수 있다면 그것도 유용하다.

# RL! No Data!
대규모 데이터셋이 없어도 (온라인) 강화학습(RL)을 통해 AI 문제를 해결할 수 있다. RL을 따르면 데이터의 가용성, 분석, 저장 및 처리와 관련된 모든 문제를 우회할 수 있지만, 이는 계산에 필요한 노력을 최소화하지는 않는다. 사실, 가장 효율적인 RL 방법조차도 탐색 과정 자체가 비용이 많이 들기 때문에 계산 부하가 크다. 게다가, 보상 함수를 구성하는 것은 종종 블랙아트(비공식적) 또는 실용적인 지혜(보다 공식적)의 형태를 띤다. 이러한 이유로, 연구자는 다양한 보상 유형(다른 하이퍼파라미터와 함께)으로 지속적으로 실험을 해야 한다.

# Small Models! No Compute!
계산 부하를 줄이기 위해 모델 규모를 축소할 수 있는 전략도 있다. 가능한 한 문제를 해결하거나 작업을 완료할 수 있는 가장 작은 모델을 생각해 볼 수 있다. 이는 실제 세계 응용 분야에서 특히 중요하며, 게임, IoT 및 자율 주행 차량과 같은 wild domains에서 사용자 옆에 AI를 배치하고 사용자가 생성하는 데이터에 AI를 배치할 수 있도록 한다. 이것은 종종 edge AI라고 불리며, AI 응용 프로그램을 네트워크의 끝에서 작동시킬 수 있기 때문에 메모리 요구 사항이 낮고 추론이 빠르게 이루어질 때 가능하다. edge AI를 위한 Neuroevolution 및 neural architecture search 및 지식 전달 방법 등의 방법이 있다.

# Work on Specialized Application Areas or Domains
특정 분야에서 혁신을 시도하는 것도 효율적인 전략이다. 적어도 산업계의 직접적인 관심을 벗어난 상대적으로 성숙한 연구 분야를 선택하여 이를 통해 혁신을 시도하는 것은 종종 성공적인 전략이다. 단, 결과가 해당 분야를 넘어 큰 영향을 미치는 것은 드물다. 게임 분야에서 AI를 연구하고 있는 우리같은 경우, 대기업이 모던 AI for games에 진지한 노력을 기울이지 않으므로 AI for games 커뮤니티를 주요 과학 커뮤니티로 삼고 있다.## Summaries

10. Finding a niche or application that does not exist yet can be a risky but potentially rewarding strategy. Look for problems or methods that are not yet considered important, or in a field that is not timely or "sexy". This high-risk, high-gain mindset may lead to a lonely path, but it could be highly rewarding in the long run.

11. Small academic teams have the advantage of being able to try things that "shouldn't work", as failure can be as instructive and valuable as success. Many important inventions and ideas in AI come from trying the "wrong" thing.

12. Large companies are often constrained by ethics and optics, but individual researchers have nothing to lose. As long as research is ethical, there is an opportunity to do research that these companies will not do. The world is full of very different people and cultures, and there is a big opportunity to explore these areas.## As an example of a project that exploits such an opportunity, one of us participated in a project critically examining the normativity of the “neutral English” in current writing support systems by creating an autocomplete system with a language model that assumes you write in the tone of Chuck Tingle, the famous author of absurd sci-fi political satire gay erotic [7].

이러한 기회를 이용하는 프로젝트의 예로, 우리 중 한 사람은 현재 쓰기 지원 시스템에서 '중립적인 영어'의 규범성을 비판적으로 검토하는 프로젝트에 참여하여, Chuck Tingle의 톤으로 쓴다고 가정한 언어 모델로 자동 완성 시스템을 만들었습니다. [7] 우리는 이 프로젝트가 아마존이나 구글에서 출판을 승인하지 않았을 것이라고 추측합니다. 이 논문 자체도 다른 예입니다.

## Similarly, you may find that you deviate from the cultural consensus in big tech companies regarding topics relating to nudity, sexuality, rudeness, religion, capitalism, communism, law and order, justice, equality, welfare, representation, history, reproduction, violence, or something else.

마찬가지로, nudity, sexuality, rudeness, religion, capitalism, communism, law and order, justice, equality, welfare, representation, history, reproduction, violence 또는 다른 주제와 관련하여 대형 기술 회사에서 문화적 합의에서 벗어나는 것을 발견할 수 있습니다.

## Being part of the applied AI world offers many benefits.

응용 AI 세계의 일원이 되면 많은 혜택이 있습니다.

## Finally, you usually gain access to more compute and, if the start-up scales up, growing access to human resources.

마지막으로, 일반적으로 더 많은 컴퓨팅 자원에 액세스하고, 스타트업이 확장되면 인적 자원에 접근할 수 있는 기회가 늘어납니다.

## Here, we might point out that both of us publish many more papers with our academic research teams than with the company we co-founded and work part-time at.

여기서 우리는 우리 둘 다 학술 연구 팀과 함께 더 많은 논문을 출판하는 것을 언급할 수 있습니다. 우리는 공동 창업하고 파트타임으로 일하는 회사보다 학교 쪽에서 더 많은 논문을 출판합니다.

## If none of the above options work for you and you still want to innovate though large scale methods that are trained on lots of data you can always collaborate with those that have them both: compute and data.

위의 옵션이 모두 작동하지 않고 여전히 많은 양의 데이터에 대해 훈련된 대규모 방법으로 혁신하고 싶다면, 언제든지 컴퓨팅과 데이터 둘 다를 가진 사람들과 협력할 수 있습니다.파트너십, 배치 또는 실험실 이전은 놀라울 정도로 효과적일 수 있다 [21,22]. 한눈에 보면, 이것이 AI 학자들에게 가장 좋은 방법으로 보이지만, 1) 생성된 지식재산권(IP)이 항상 공개되지 않을 수 있고 2) 모두가 AI 산업 기반 실험실에서 일할 수는 없거나 원하지 않을 수 있다는 것이다. 일부 사람들은 혁신이 산업이 지원하는 공공기관에 의해 주도될 필요가 있다고 주장할 수도 있다. 따라서 대학은 교육하는 재능 있는 AI 연구자(학자 및 학생) 및 그들이 생성하는 IP 일부를 유지할 책임이 있다. 그렇지 않으면 AI 교육과 연구는 결국 대학 환경 내에서 무의미해질 것이다. 다음으로, 산업 기업과 대학이 어떻게 도움을 줄 수 있는지에 대해 자세히 살펴보자. (Markdown format: # partnerships, placements or lab transfers can be astonishing [21,22]...)# trying and failing and promote high-risk high-gain funding schemes and research initiatives. It is then likely that funding agencies will follow the trend and invest even more on basic and blue sky research.

위험한 고수익 기금 조성 및 연구 계획을 추진하면서 시도하고 실패하는 것은 매우 가능합니다. 그러면 자금 기관들이 추세를 따르고 기본 및 블루 스카이 연구에 더 많은 투자를 할 가능성이 있습니다.

# Parting Words

우리는 몇 가지 목적으로이 편지를 작성했습니다. 첫째, 커뮤니티로서 공통의 원인 (및 집단적인 치료?)을 찾는 희망과 함께 다른 AI 연구자들과 우려 사항을 공유하려는 것입니다. 

둘째, 우리 자신의 경험과 학계 및 산업 AI 행사에서 나온 논의를 기반으로 한 지침 세트를 제공하는 것입니다. 

셋째, 모두에게 더 효율적인 전략을 위한 아이디어를 촉진하고 열린 대화를 자극하는 것입니다. 

아마도 우리가 여기서 논의 한 전략 목록은 가능한 모든 가능성을 포함하고 있지는 않지만, 우리는 그것들이 우리가 생각하기에 매우 적시적인 대화의 씨앗이라고 믿습니다.[13] Scott Reed, Konrad Zolna, Emilio Parisotto, Sergio Gomez Colmen arejo, Alexander Novikov, Gabriel Barth-Maron, Mai Gimenez, Yury Sulsky, Jackie Kay, Jost Tobias Springenberg, et al. A generalist agent. arXiv preprint arXiv:2205.06175 , 2022.
[14] Sebastian Risi and Julian Togelius. Increasing generality in machin e learning through procedural content generation. Nature Machine Intelligence , 2(8):428–436, 2020.
[15] Olga Russakovsky, Jia Deng, Hao Su, Jonathan Krause, Sanje ev Satheesh, Sean Ma, Zhiheng Huang, Andrej Karpathy, Aditya Khosla, Michael Bernstein, et al. Imagenet large scale visual recognition challenge. International journal of computer vision , 115:211–252, 2015.
[16] Roy Schwartz, Jesse Dodge, Noah A Smith, and Oren Etzioni. Gr een ai.Communications of the ACM , 63(12):54–63, 2020.
[17] Nur Muhammad Shaﬁullah, Zichen Cui, Ariuntuya Arty Altanzaya, and Lerrel Pinto. Behavior transformers: Cloning kmodes with one stone. Advances in neural information processing systems , 35:22955–22968, 2022.
[18] Richard Sutton. The bitter lesson. Incomplete Ideas (blog) , 13(1), 2019.
[19] Adaptive Agent Team, Jakob Bauer, Kate Baumli, Satinder Bave ja, Feryal Behbahani, Avishkar Bhoopchand, Nathalie Bradley-Schmieg, Michael Chang, Natalie Clay , Adrian Collister, et al.
Human-timescale adaptation in an open-ended task space. arXiv preprint arXiv:2301.07608 , 2023.
[20] Julian Togelius, Georgios N Yannakakis, Kenneth O Stanley, and C ameron Browne. Search-based procedural content generation: A taxonomy and survey. IEEE Transactions on Computational Intelligence and AI in Games , 3(3):172–186, 2011.
[21] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, /suppress Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. Advances in neural information processing systems , 30, 2017.
[22] Ziyu Wang, Tom Schaul, Matteo Hessel, Hado Hasselt, Marc Lanc tot, and Nando Freitas. Dueling network architectures for deep reinforcement learning. In International conference on machine learning , pages 1995–2003. PMLR, 2016.
[23] Georgios N Yannakakis and Julian Togelius. Experience-driven pr ocedural content generation.
IEEE Transactions on Aﬀective Computing , 2(3):147–161, 2011.
9
- completion_tokens: 5710
- prompt_tokens: 7025
- total_cost: 0.02547
- total_tokens: 12735
