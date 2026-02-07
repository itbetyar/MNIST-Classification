# MNIST-ANN-classic | Kézzel írott számok felismerése
Canonical Basic Neural Network - itbetyar.hu

<img src="https://raw.githubusercontent.com/itbetyar/MNIST-Classification/refs/heads/main/mnist_img.webp" alt="MNIST Demo" width="350">

⭐ Ha tetszik a projekt, adj neki egy csillagot a GitHub-on!

| IT Betyár Demo | GitHub Repository | Hugging Face Demo | AI Tanfolyam |
| :---: | :---: | :---: | :---: |
| [![🚀 IT Betyár Demo](https://img.shields.io/badge/🚀_IT_Betyár-Demo_MNIST-orange)](https://itbetyar.hu/project/mnist-karakter-felismero-projekt/) | [![GitHub](https://img.shields.io/badge/GitHub-MNIST_Repo-f0f0f0?logo=github&logoColor=black)](https://github.com/itbetyar/MNIST-Classification) | [![🤗 Hugging Face](https://img.shields.io/badge/🤗_Hugging_Face-MNIST_Space-FFD21E)](https://huggingface.co/spaces/itbetyar/2-MNIST-Classifier) | [![🎓 AI Tanfolyam](https://img.shields.io/badge/🎓_AI_Tanfolyam-itbetyar.hu-28a745)](https://itbetyar.hu/mesterseges-intelligencia-fejleszto-tanfolyam/) |


## 📖 Leírás
Ez a projekt egy **alapszintű Artificial Neural Network (ANN)** hálót használ kézzel írott számjegyek (0-9) osztályozására. A modell az MNIST adatbázison tanul, amely 70,000 db 28x28 pixeles képet tartalmaz.

🔗 **Élő demo és projektleírás >>**  [![🚀 IT Betyár Demo](https://img.shields.io/badge/🚀_IT_Betyár-Demo_MNIST-orange)](https://itbetyar.hu/project/mnist-karakter-felismero-projekt/) 

## 🎯 Funkciók
- **10 számjegy felismerése** (0-9) - MNIST adatbázis alapján
- **Egyszerű felület** - Gradio alapú GUI interfész
- **Példa számjegyek** - Tesztképek azonnali kipróbáláshoz

## 🧠 Modell részletek
### Technikai specifikáció
| Paraméter | Érték |
|-----------|-------|
| **Modell típus** | ANN - Mesterséges Neurális Háló (Fully Connected) |
| **Rétegszám** | 4 réteg (input, 2hidden, output) |
| **Paraméterek** | ~100,000 paraméter |
| **Modell fájlméret** | ~1.4 MB |
| **Tanító adatszett** | MNIST (60,000 tanító, 10,000 teszt kép) |
| **Aktivációs függvény** | ReLU (hidden), Softmax (output) |
| **Pontosság** | ~97-98% a teszt adaton |

### ANN architektúra
<img src="https://raw.githubusercontent.com/itbetyar/MNIST-Classification/refs/heads/main/mnist_architecture.webp" alt="ANN Architecture" width="350">

### Mai viszonyítás
<table>
  <thead>
    <tr>
      <th>Modell</th>
      <th>Év</th>
      <th>Rétegszám</th>
      <th>Paraméterek</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Egyszerű ANN (MNIST)</strong></td>
      <td>1998+</td>
      <td>3 réteg</td>
      <td>~100 ezer</td>
    </tr>
    <tr>
      <td><strong>ResNet-50</strong></td>
      <td>2015</td>
      <td>50 réteg</td>
      <td>~25 millió</td>
    </tr>
    <tr>
      <td><strong>GPT-4</strong></td>
      <td>2023</td>
      <td>120+ transformer réteg</td>
      <td>~1.7 trillió</td>
    </tr>
    <tr>
      <td><strong>Stable Diffusion</strong></td>
      <td>2022</td>
      <td>-</td>
      <td>~890 millió</td>
    </tr>
  </tbody>
</table>


**Összefoglalva:** Az MNIST ANN a legklasszikusabb "Hello World" példa a neurális hálók világában - egyszerű, hatékony, és tökéletes az alapok megtanulásához! 🎯

## 🚀 Történet
**MNIST adatbázis:** Yann LeCun és csapata, 1998  
**Módosított verzió:** Modified National Institute of Standards and Technology  

Az MNIST az egyik legismertebb benchmark adatbázis a gépi tanulásban. Minden kezdő data scientist ezen tanulja meg a neurális hálók alapjait.


🔗 **Tanfolyam:** [itbetyar.hu/mesterseges-intelligencia-fejleszto-tanfolyam](https://itbetyar.hu/mesterseges-intelligencia-fejleszto-tanfolyam/)

## 🌐 Deployment
Az alkalmazás elérhető Hugging Face Spaces-en / Streamlit Cloud-on:
- **Demo URL:** [https://huggingface.co/spaces/itbetyar/mnist-ann-classifier](https://huggingface.co/spaces/itbetyar/mnist-ann-classifier)



## 👨‍💻 Szerző
**IT Betyár**  
- Website: [itbetyar.hu](https://itbetyar.hu)
- GitHub: [@itbetyar](https://github.com/itbetyar)

---

⭐ Ha tetszik a projekt, adj neki egy csillagot a GitHub-on!

| IT Betyár Demo | GitHub Repository | Hugging Face Demo | AI Tanfolyam |
| :---: | :---: | :---: | :---: |
| [![🚀 IT Betyár Demo](https://img.shields.io/badge/🚀_IT_Betyár-Demo_MNIST-orange)](https://itbetyar.hu/project/mnist-karakter-felismero-projekt/) | [![GitHub](https://img.shields.io/badge/GitHub-MNIST_Repo-f0f0f0?logo=github&logoColor=black)](https://github.com/itbetyar/MNIST-Classification) | [![🤗 Hugging Face](https://img.shields.io/badge/🤗_Hugging_Face-MNIST_Space-FFD21E)](https://huggingface.co/spaces/itbetyar/2-MNIST-Classifier) | [![🎓 AI Tanfolyam](https://img.shields.io/badge/🎓_AI_Tanfolyam-itbetyar.hu-28a745)](https://itbetyar.hu/mesterseges-intelligencia-fejleszto-tanfolyam/) |


**Frissítve:** 2026.02
