# MNIST-ANN-classic | Kézzel írott számok felismerése | IT Betyár
Canonical Basic Neural Network - itbetyar.hu

<img src="https://raw.githubusercontent.com/itbetyar/MNIST-ANN-classic/refs/heads/main/img-assets/mnist-demo.webp" alt="MNIST Demo" width="350">


## 📖 Leírás
Ez a projekt egy **alapszintű Artificial Neural Network (ANN)** hálót használ kézzel írott számjegyek (0-9) osztályozására. A modell az MNIST adatbázison tanul, amely 70,000 db 28x28 pixeles képet tartalmaz.

🔗 **Élő demo projektleírás:** [itbetyar.hu/project/mnist-ann-classification](https://itbetyar.hu/project/mnist-ann-classification/)

## 🎯 Funkciók
- **10 számjegy felismerése** (0-9) - MNIST adatbázis alapján
- **Valós idejű predikció** - Rajzolj egy számot és azonnal látod az eredményt
- **Egyszerű felület** - Gradio/Streamlit alapú webes interfész
- **Példa számjegyek** - Tesztképek azonnali kipróbáláshoz

## 🧠 Modell részletek
### Technikai specifikáció
| Paraméter | Érték |
|-----------|-------|
| **Modell típus** | ANN - Mesterséges Neurális Háló (Fully Connected) |
| **Rétegszám** | 3 réteg (input, hidden, output) |
| **Paraméterek** | ~100,000 paraméter |
| **Modell fájlméret** | ~400 KB |
| **Tanító adatszett** | MNIST (60,000 tanító, 10,000 teszt kép) |
| **Aktivációs függvény** | ReLU (hidden), Softmax (output) |
| **Pontosság** | ~97-98% teszt adaton |

### ANN architektúra
<img src="https://raw.githubusercontent.com/itbetyar/MNIST-ANN-classic/refs/heads/main/img-assets/ann-architecture.webp" alt="ANN Architecture" width="350">

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

### Neurális háló struktúra
<img src="https://raw.githubusercontent.com/itbetyar/MNIST-ANN-classic/refs/heads/main/img-assets/mnist-network-structure.webp" alt="Network Structure" width="500">

**Összefoglalva:** Az MNIST ANN a legklasszikusabb "Hello World" példa a neurális hálók világában - egyszerű, hatékony, és tökéletes az alapok megtanulásához! 🎯

## 🚀 Történet
**MNIST adatbázis:** Yann LeCun és csapata, 1998  
**Módosított verzió:** Modified National Institute of Standards and Technology  

Az MNIST az egyik legismertebb benchmark adatbázis a gépi tanulásban. Minden kezdő data scientist ezen tanulja meg a neurális hálók alapjait.

## 🛠️ Telepítés és futtatás
### Követelmények
- Python 3.11
- pip package manager

### Függőségek telepítése
```bash
pip install -r requirements.txt
```

**requirements.txt tartalma:**
```
tensorflow==2.15.0
# VAGY
torch==2.10.0
numpy==1.26.0
gradio==5.9.1
# VAGY
streamlit==1.40.0
```

### Alkalmazás indítása
```bash
python app.py
```

A Gradio/Streamlit interfész automatikusan elindul a böngészőben (általában `http://localhost:7860`).

## 📁 Projekt struktúra
```
.
├── app.py                 # Fő alkalmazás
├── model.py              # Modell definíció és betöltés
├── train.py              # Modell tanítási script (opcionális)
├── requirements.txt      # Python függőségek
├── mnist_model.h5        # Betanított modell
├── img-assets/           # README képek
└── README.md
```

## 💻 Használat
1. **Rajzolj egy számot** a vászonra (0-9 között)
2. **Predikció** - A modell azonnal felismeri a számjegyet
3. **Eredmény** - Látod a predikciót és a valószínűségi értékeket
4. **Törlés** - Próbálj újabb számokat

## 🎓 Oktatási célok
Ez a projekt az **IT Betyár Mesterséges Intelligencia Fejlesztő Tanfolyam** része, amely bemutatja:

- Neurális hálók alapjai (ANN)
- MNIST adatbázis használata
- TensorFlow/PyTorch alapok
- Modell tanítás és értékelés
- AI alkalmazások deployment-je

🔗 **Tanfolyam:** [itbetyar.hu/mesterseges-intelligencia-fejleszto-tanfolyam](https://itbetyar.hu/mesterseges-intelligencia-fejleszto-tanfolyam/)

## 🌐 Deployment
Az alkalmazás elérhető Hugging Face Spaces-en / Streamlit Cloud-on:
- **Demo URL:** [https://huggingface.co/spaces/itbetyar/mnist-ann-classifier](https://huggingface.co/spaces/itbetyar/mnist-ann-classifier)

## 📊 Tanítási eredmények
```
Epoch 1/10 - Loss: 0.35, Accuracy: 89%
Epoch 5/10 - Loss: 0.12, Accuracy: 96%
Epoch 10/10 - Loss: 0.08, Accuracy: 97.5%

Test Accuracy: 97.8%
```

## 📝 License
MIT License - lásd a [LICENSE](LICENSE) fájlt a részletekért.

## 👨‍💻 Szerző
**IT Betyár**  
- Website: [itbetyar.hu](https://itbetyar.hu)
- GitHub: [@itbetyar](https://github.com/itbetyar)

---

⭐ Ha tetszik a projekt, adj neki egy csillagot a GitHub-on!

**Frissítve:** 2026.02
