from Bio import Entrez as E, SeqIO
import matplotlib.pyplot as P, csv, io

E.email, E.api_key = input(), input()
mnl, mxl, tid, n = map(int, [input(), input(), input(), input()])

s = E.read(E.esearch("nucleotide", term=f"txid{tid}[Organism]", usehistory="y"))
if int(s['Count']):
    h = E.efetch("nucleotide", rettype="gb", retmode="text", retstart=0, retmax=min(n, 500), webenv=s['WebEnv'], query_key=s['QueryKey'])
    d = h.read();open(f"t{tid}.gb", "w").write(d)
    if (r := [{"accession": x.id, "length": len(x.seq), "description": x.description} for x in
              SeqIO.parse(io.StringIO(d), "genbank") if mnl <= len(x.seq) <= mxl]):
        with open(f"{tid}.csv", "w", newline='') as f: csv.DictWriter(f, r[0]).writerows([r[0]] + r)
        r.sort(key=lambda x: x["length"], reverse=True)
        P.plot([x["accession"] for x in r], [x["length"] for x in r], 'o')
        P.xticks(rotation=90);P.tight_layout();P.savefig(f"{tid}.png")