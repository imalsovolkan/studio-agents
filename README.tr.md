# Studio Agents

Claude Code için on agent'tan oluşan bir tasarım ve ürün ekibi. Agent'lar yalnızca sen adlarını yazıp çağırdığında çalışıyor ve bir aşama, ancak senin onayın kayda geçtiğinde kapanıyor.

[English README](README.md)

## Neden böyle
Agent ekiplerinin çoğu, bir hedef verildiğinde işi kendi aralarında devreden bir akış olarak çalışıyor. Bu ekip tersini yapıyor: sen bir agent'ı adıyla çağırmadıkça hiçbir şey çalışmıyor, her agent tek bir aşamayı yapıp duruyor ve projeyi ilerleten tek şey `decisions.md` dosyasına senin onayınla yazılan satır oluyor.

Ekip üç işi birbirinden ayırıyor:

- İşin kendisini dokuz uzman agent yapıyor.
- Denetimi Studio Lead yapıyor ve uzmanlık işlerine hiç girmiyor.
- Onayı sen veriyorsun ve bir agent'ın ilettiği onay onay sayılmıyor.

## Önce kendi kurallarını yaz
Ekip, senin yazdığın tek bir dosyaya göre çalışıyor: `studio/house_rules.md`. Bu dosyada her seferinde aynı şekilde verdiğin tasarım kararları, nedenleri ve nasıl kontrol edilecekleriyle birlikte duruyor. Her agent işe başlamadan önce bu dosyayı okuyor, denetim yapan agent'lar çıktıları bu kurallara göre inceliyor ve hiçbir agent dosyayı değiştiremiyor.

Dosya dört başlangıç kuralıyla ve boş bir "bilinen sorunlar" kaydıyla geliyor. Bu kuralları tutabilir, değiştirebilir ya da silebilirsin, sonra kendi kuralını ekleyebilirsin. Bir kuralı yazmakta zorlanıyorsan o karar henüz bir kurala dönüşmemiş olabilir.

## Hızlı başlangıç
Gereken tek şey Claude Code. Figma isteğe bağlı ve yalnızca üç agent için gerekiyor.

```bash
git clone https://github.com/imalsovolkan/studio-agents.git
cd studio-agents
claude
```

Claude Code içinde:

```
/agents
@agent-studio-lead status for projects/example-app
```

`/agents` on agent'ı listelemeli. İkinci komut, denemen için eklenmiş kurgusal bir projenin durumunu okuyup raporluyor. Kurulumun geri kalanını `studio/first_run.md` dosyasındaki altı kontrolle sınayabilirsin.

Raporları ve sohbeti Türkçe almak için `CLAUDE.md` içindeki satırı `Owner language: Turkish` olarak değiştirmen yeterli.

## Kurallar
1. Agent'lar yalnızca sen adlarını yazdığında çalışıyor ve hiçbir agent başka bir agent'ı başlatmıyor.
2. Her agent tek bir aşamayı yapıyor, tek bir çıktı veriyor ve bir devir notu bırakıyor.
3. Agent önce kısa bir plan yazıyor ve senin "devam" demeni bekliyor.
4. Her agent yalnızca kendi klasörüne yazıyor. `project_state.md` ve `decisions.md` dosyalarını, sen onayladıktan sonra yalnızca Studio Lead ya da ana oturum yazıyor.
5. Bir agent'ın ilettiği onay onay sayılmıyor.
6. Agent'lar bilgi, sayı, alıntı ya da sonuç uydurmuyor. Varsayımlar `[Assumption]`, doğrulanmamış bilgiler `[Unverified]` olarak işaretleniyor.
7. Her agent işe başlamadan önce `studio/house_rules.md` dosyasını okuyor ve ona uyuyor.
8. Hiçbir agent kendi işini denetlemiyor. Ekranları, onları yapmayan iki agent inceliyor: UX Architect eleştiri ve sezgisel değerlendirmeyi, Design System Builder ise erişilebilirlik ve sistem uyumunu üstleniyor.

Hangi kuralın teknik olarak zorlandığı, hangisinin yalnızca yazılı olduğu İngilizce README'deki tabloda duruyor.

## Lisans
MIT. Ayrıntılar `LICENSE` dosyasında.
